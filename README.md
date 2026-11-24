API Test Automation Project
신세계 QA Mall의 상품 검색 기능을 대상으로 Python과 Pytest를 활용한 API 테스트 자동화 프로젝트입니다.
HTTP 요청을 통해 상품 검색 페이지의 응답을 수신하고, HTML 내부에 포함된 JSON 데이터를 추출하여 상품 정보를 검증합니다.


⸻


1. 프로젝트 소개
프로젝트 목표
상품 검색 기능의 HTTP 응답 검증
HTML 내부 JSON 데이터 추출
정상 및 예외 검색 시나리오 검증
JSON Schema 기반 데이터 검증
테스트 결과 리포트 및 로그 관리
테스트 대상
서비스: 신세계 QA Mall
기능: 상품 검색
환경: QA


⸻


2. 기술 스택
Language: Python
HTTP Client: Requests
Test Framework: Pytest
Data Validation: JSON Schema
Test Report: pytest-html
Test Data: JSON
Configuration: JSON


⸻


3. 프로젝트 구조
프로젝트는 설정, 테스트 데이터, 테스트 코드, 공통 유틸리티로 구성되어 있습니다.

config/
config.json: 공통 설정 관리
environments/qa.json: QA 환경별 서버 주소 설정

reports/
search_response.html: 검색 응답 HTML 자료
test_report.html: 테스트 실행 결과 리포트
test.log: API 요청 및 응답 로그

schemas/
product_schema.json: 상품 데이터 구조 검증 스키마

test_data/
products.json: 정상 검색 테스트 데이터
negative_cases.json: 예외 검색 테스트 데이터

tests/
test_connection.py: 검색 페이지 연결 테스트
test_negative_search.py: 예외 검색 테스트
test_product_search.py: 상품 검색 및 데이터 검증 테스트
test_search_response.py: 검색 응답 및 상품 데이터 추출 테스트

utils/
api_client.py: HTTP 요청 및 세션 관리
config.py: 설정 파일 로드 및 관리
data_loader.py: 테스트 데이터 로드
html_parser.py: HTML 내부 JSON 추출
product_parser.py: 상품 정보 추출 및 정규화
response_validator.py: 응답 및 상품 데이터 검증
schema_validator.py: JSON Schema 검증

Root Files
.env.example: 환경 변수 설정 예시
.gitignore: Git 추적 제외 파일 관리
conftest.py: Pytest Fixture 관리
pytest.ini: Pytest 실행 설정
requirements.txt: 프로젝트 의존성 목록
README.md: 프로젝트 문서


⸻


4. 주요 테스트 항목
4.1 정상 검색 테스트
HTTP 상태 코드 검증
API 응답 코드 검증
상품 검색 결과 존재 여부 확인
상품 필수 필드 검증
상품 가격 데이터 형식 검증
검색어와 상품명 일치 여부 검증
JSON Schema 기반 데이터 구조 검증
4.2 예외 검색 테스트
빈 검색어 입력
존재하지 않는 상품 검색
예상 검색 결과 개수 검증
4.3 연결 및 응답 테스트
검색 페이지 연결 확인
HTTP 응답 형식 확인
HTML 내부 JSON 데이터 추출
상품 데이터 파싱 확인


⸻


5. 실행 환경 설정
5.1 프로젝트 Clone
git clone <repository-url>
cd api-qa
5.2 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate
5.3 라이브러리 설치
pip install -r requirements.txt
5.4 환경 설정
config/environments/qa.json에서 QA 서버 주소 설정
.env.example을 참고하여 필요한 환경 변수 설정


⸻


6. 테스트 실행
전체 테스트 실행
pytest
특정 테스트 실행
pytest tests/test_product_search.py
예외 검색 테스트 실행
pytest tests/test_negative_search.py


⸻


7. 테스트 결과 및 로그
테스트 실행 후 reports/ 디렉터리에서 결과를 확인할 수 있습니다.
test_report.html: 테스트 실행 결과 리포트
test.log: API 요청 및 응답 로그
search_response.html: 검색 응답 HTML 자료
HTML 리포트를 브라우저에서 열어 테스트별 성공 및 실패 결과를 확인할 수 있습니다.


⸻


8. 주요 구현 내용
APIClient: HTTP 요청 및 세션 관리
Config: 환경별 설정 관리
DataLoader: JSON 테스트 데이터 로드
HtmlParser: HTML 내부 JSON 데이터 추출
ProductParser: 상품 정보 추출 및 정규화
ResponseValidator: 응답 및 상품 데이터 검증
SchemaValidator: JSON Schema 검증
Pytest Fixtures: 테스트 환경 및 클라이언트 관리
추가 구현 사항:
Parametrize를 활용한 검색 조건별 반복 테스트
pytest-html을 활용한 HTML 테스트 리포트 생성
logging을 활용한 API 요청 및 응답 기록


⸻


9. 향후 개선 방향
추가 API 엔드포인트 테스트 확장
CI/CD 기반 테스트 자동 실행
테스트 실패 시 원인 분석 및 리포트 개선
