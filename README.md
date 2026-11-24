API Test Automation
신세계 QA Mall의 상품 검색 기능을 대상으로 Python과 Pytest를 활용한 API 테스트 자동화 프로젝트입니다.
HTTP 요청부터 응답 데이터 추출, 상품 정보 검증, 테스트 결과 리포트 생성까지 자동화하는 것을 목표로 합니다.


⸻


1. Project Overview
목적
상품 검색 기능의 HTTP 응답 검증
HTML 응답 내부 JSON 데이터 추출
상품 정보 및 데이터 구조 검증
정상 및 예외 검색 시나리오 테스트
테스트 결과 및 실행 로그 관리
테스트 대상
대상 서비스: 신세계 QA Mall
대상 기능: 상품 검색
테스트 환경: QA


⸻


2. Tech Stack
Category
Technology
Language
Python
HTTP Client
Requests
Test Framework
Pytest
Data Validation
JSON Schema
Test Report
pytest-html
Test Data
JSON
Configuration
JSON


⸻


3. Project Structure
api-qa/
│
├── config/
│   ├── environments/
│   │   └── qa.json
│   └── config.json
│
├── reports/
│   ├── search_response.html
│   ├── test_report.html
│   └── test.log
│
├── schemas/
│   └── product_schema.json
│
├── test_data/
│   ├── negative_cases.json
│   └── products.json
│
├── tests/
│   ├── test_connection.py
│   ├── test_negative_search.py
│   ├── test_product_search.py
│   └── test_search_response.py
│
├── utils/
│   ├── api_client.py
│   ├── config.py
│   ├── data_loader.py
│   ├── html_parser.py
│   ├── product_parser.py
│   ├── response_validator.py
│   └── schema_validator.py
│
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


⸻


4. Test Coverage
4.1 Connection Test
검색 페이지 HTTP 연결 확인
HTTP 상태 코드 검증
Content-Type 검증
응답 데이터 존재 여부 확인
4.2 Product Search Test
상품 검색 결과 존재 여부 검증
API 응답 코드 검증
상품 필수 필드 검증
상품 가격 데이터 형식 검증
검색어와 상품명 일치 여부 검증
JSON Schema 기반 데이터 구조 검증
4.3 Negative Test
빈 검색어 입력
존재하지 않는 상품 검색
예상 검색 결과 개수 검증
4.4 Response Parsing Test
HTML 응답 내부 JSON 추출
상품 목록 영역 식별
상품 정보 추출 및 정규화


⸻


5. Test Execution
환경 설정
git clone <repository-url>
cd api-qa
가상환경 생성 및 활성화:
python -m venv .venv
.venv\Scripts\activate
라이브러리 설치:
pip install -r requirements.txt
전체 테스트 실행
pytest
특정 테스트 실행
pytest tests/test_product_search.py


⸻


6. Test Report & Logging
테스트 실행 후 reports/ 디렉터리에 결과가 생성됩니다.
File
Description
test_report.html
HTML 테스트 결과 리포트
test.log
API 요청 및 응답 로그
search_response.html
검색 응답 HTML 자료
HTML 리포트를 통해 테스트 성공 및 실패 결과 확인
로그를 통해 API 요청, 응답 상태 및 예외 발생 내역 확인


⸻


7. Architecture & Implementation
Component
Responsibility
APIClient
HTTP 요청 및 세션 관리
Config
환경별 설정 관리
DataLoader
JSON 테스트 데이터 로드
HtmlParser
HTML 내부 JSON 데이터 추출
ProductParser
상품 정보 추출 및 정규화
ResponseValidator
응답 및 상품 데이터 검증
SchemaValidator
JSON Schema 검증
Pytest Fixtures
테스트 환경 및 클라이언트 관리


⸻


8. Future Improvements
추가 API 엔드포인트 테스트 확장
CI/CD 기반 테스트 자동 실행
테스트 실패 시 리포트 및 로그 분석 기능 개선