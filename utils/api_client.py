import logging

import requests


logger = logging.getLogger(__name__)


class APIClientError(Exception):
   """API 요청 과정에서 발생하는 사용자 정의 예외"""
   pass


class APIClient:

   def __init__(self, base_url, timeout=10):
       self.base_url = base_url.rstrip("/")
       self.timeout = timeout

       self.session = requests.Session()
       self.session.headers.update({
           "Accept": "application/json"
       })

   def set_token(self, token):
       if not token:
           raise ValueError("인증 토큰이 비어 있습니다.")

       self.session.headers.update({
           "Authorization": f"Bearer {token}"
       })

   def clear_token(self):
       self.session.headers.pop("Authorization", None)

   @property
   def is_authenticated(self):
       return "Authorization" in self.session.headers

   def request(self, method, endpoint, **kwargs):
       url = f"{self.base_url}/{endpoint.lstrip('/')}"
       method = method.upper()

       logger.info("API 요청 시작: %s %s", method, url)

       try:
           response = self.session.request(
               method=method,
               url=url,
               timeout=self.timeout,
               **kwargs
           )

           logger.info(
               "API 응답 수신: %s %s - Status: %s",
               method,
               url,
               response.status_code
           )

           return response

       except requests.exceptions.RequestException as e:
           logger.exception(
               "API 요청 실패: %s %s",
               method,
               url
           )

           raise APIClientError(
               f"{method} 요청 실패: {e}"
           ) from e

   def get(self, endpoint, params=None):
       return self.request(
           "GET",
           endpoint,
           params=params
       )

   def post(self, endpoint, json=None, data=None):
       if json is not None and data is not None:
           raise ValueError(
               "json과 data를 동시에 전달할 수 없습니다."
           )

       return self.request(
           "POST",
           endpoint,
           json=json,
           data=data
       )

   def put(self, endpoint, json=None):
       return self.request(
           "PUT",
           endpoint,
           json=json
       )

   def patch(self, endpoint, json=None):
       return self.request(
           "PATCH",
           endpoint,
           json=json
       )

   def delete(self, endpoint):
       return self.request(
           "DELETE",
           endpoint
       )

   def close(self):
       self.session.close()
       logger.info("API 세션 종료: %s", self.base_url)