#Pytest에서 공통으로 사용할 설정과 Fixture를 관리하는 파일

import pytest
from utils.api_client import APIClient
from utils.config import Config

@pytest.fixture(scope="session") #fixture:테스트가 실행되기 전에 필요한 객체나 데이터를 준비해 주는 기능
#session: pytest 실행 세션 동안 한 번 생성하고 재사용
#기본값인 function: 테스트 함수마다 새로 생성 
def config():
   """테스트 세션 전체에서 사용할 공통 설정"""
   return Config(env="qa")

@pytest.fixture
def search_client(config):#앞서 만든 config fixture 전달받는다는 의미
   """상품 검색 페이지 요청용 클라이언트"""
   client = APIClient(
       base_url=config.get("search_base_url"),
       timeout=config.get("timeout", default=15)
   )
   yield client
   #return을 사용했을때: 객체를 전달하고 fixture실행 끝남 > 뒤에 작성한 정리 코드가 실행되지 않음
   #yield을 사용했을때: 객체를 테스트에 전달 > 테스가 실행되는 동안 대기 > 테스트가 끝나면 아래쪽 정리 코드 실행
   #왜 필요? HTTP 세션을 사용한 뒤 정리필요, 테스트 간 리소스 간섭을 줄일 수 있음, 테스트가 실패해도 정리 코드 실행
   client.close()

@pytest.fixture
def product_api_client(config):
   """상품 목록 JSON API 요청용 클라이언트"""
   client = APIClient(
       base_url=config.get("product_api_base_url"),
       timeout=config.get("timeout", default=15)
   )
   yield client
   client.close()