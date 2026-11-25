import pytest
import requests

from utils.api_client import APIClient, APIClientError


@pytest.fixture
def api_client():
   client = APIClient(
       base_url="https://example.com",
       timeout=1
   )
   yield client
   client.close()


def test_api_timeout(api_client, monkeypatch): #monkeypatch:실제 API 요청 대신 가짜 동작을 주입
   def mock_request(*args, **kwargs): #mock_request: 가짜 API 요청 함수
       raise requests.exceptions.Timeout("요청 시간 초과") #Timeout: 요청 시간 초과 상황 재현

   monkeypatch.setattr(
       api_client.session,
       "request",
       mock_request
   )

   with pytest.raises(APIClientError):
       api_client.get("/test")


def test_api_connection_error(api_client, monkeypatch): #ConnectionError: 서버 연결 실패 재현
   def mock_request(*args, **kwargs):
       raise requests.exceptions.ConnectionError("연결 실패")

   monkeypatch.setattr(
       api_client.session,
       "request",
       mock_request
   )

   with pytest.raises(APIClientError): #APIClientError: APIClient가 변환환 예외 확인
       api_client.get("/test")


def test_api_404_response(api_client, monkeypatch):
   mock_response = requests.Response() #requests.Response(): 가짜 HTTP 응답 생성
   mock_response.status_code = 404

   def mock_request(*args, **kwargs):
       return mock_response

   monkeypatch.setattr(
       api_client.session,
       "request",
       mock_request
   )

   response = api_client.get("/not-found")

   assert response.status_code == 404


def test_api_500_response(api_client, monkeypatch):
   mock_response = requests.Response()
   mock_response.status_code = 500

   def mock_request(*args, **kwargs):
       return mock_response

   monkeypatch.setattr(
       api_client.session,
       "request",
       mock_request
   )

   response = api_client.get("/server-error")

   assert response.status_code == 500

def test_set_token(api_client):
    api_client.set_token("test_token")

    assert api_client.is_authenticated is True
    assert api_client.session.headers["Authorization"] == "Bearer test_token"

def test_clear_token(api_client):
    api_client.set_token("test-token")

    api_client.clear_token()

    assert api_client.is_authenticated is False

@pytest.mark.parametrize("token", ["", None])
def test_set_empty_token(api_client, token):
    with pytest.raises(ValueError):
        api_client.set_token(token)

def test_post_json_and_data_together(api_client):
    with pytest.raises(ValueError):
        api_client.post(
            "/test",
            json={"name": "test"},
            data={"name": "test"}
        )