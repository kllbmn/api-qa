API Test Automation Project
1. 프로젝트 소개
신세계 QA Mall의 상품 검색 기능을 대상으로 Python과 Pytest를 활용한 API 테스트 자동화 프로젝트입니다.
HTTP 요청을 통해 상품 검색 페이지의 응답을 수신하고, HTML 내부에 포함된 JSON 데이터를 추출하여 상품 정보를 검증합니다.
프로젝트 목표
상품 검색 기능의 HTTP 응답 검증
HTML 내부 JSON 데이터 추출
정상 및 예외 검색 시나리오 검증
JSON Schema 기반 데이터 검증
테스트 결과 리포트 및 로그 관리
2. 기술 스택
Language: Python
HTTP Client: Requests
Test Framework: Pytest
Data Validation: JSON Schema
Test Report: pytest-html
Test Data: JSON
Configuration: JSON
3. 프로젝트 구조
api-qa/
├── config/
│   ├── environments/
│   │   └── qa.json
│   └── config.json
├── reports/
│   ├── search_response.html
│   ├── test_report.html
│   └── test.log
├── schemas/
│   └── product_schema.json
├── test_data/
│   ├── negative_cases.json
│   └── products.json
├── tests/
│   ├── test_connection.py
│   ├── test_negative_search.py
│   ├── test_product_search.py
│   └── test_search_response.py
├── utils/
│   ├── api_client.py
│   ├── config.py
│   ├── data_loader.py
│   ├── html_parser.py
│   ├── product_parser.py
│   ├── response_validator.py
│   └── schema_validator.py
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
4. 주요 테스트 항목
정상 검색 테스트
HTTP 상태 코드 검증
API 응답 코드 검증
상품 검색 결과 존재 여부 확인
상품 필수 필드 검증
상품 가격 데이터 형식 검증
검색어와 상품명 일치 여부 검증
JSON Schema 기반 데이터 구조 검증
예외 검색 테스트
빈 검색어 입력
존재하지 않는 상품 검색
예상 검색 결과 개수 검증
연결 및 응답 테스트
검색 페이지 연결 확인
HTTP 응답 형식 확인
HTML 내부 JSON 데이터 추출
상품 데이터 파싱 확인
5. 실행 환경 설정
1) 프로젝트 Clone
git clone <repository-url>
cd api-qa
2) 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate
3) 라이브러리 설치
pip install -r requirements.txt
4) 환경 설정
config/environments/qa.json에서 QA 서버 주소 설정
.env.example을 참고하여 필요한 환경 변수 설정
6. 테스트 실행
전체 테스트 실행:
pytest
특정 테스트 실행:
pytest tests/test_product_search.py
예외 검색 테스트 실행:
pytest tests/test_negative_search.py
7. 테스트 결과 및 로그
테스트 실행 후 reports 폴더에서 결과를 확인할 수 있습니다.
test_report.html: 테스트 실행 결과 리포트
test.log: API 요청 및 응답 로그
search_response.html: 검색 응답 HTML 자료
HTML 리포트를 브라우저에서 열어 테스트별 성공 및 실패 결과를 확인할 수 있습니다.
8. 주요 구현 내용
API Client를 별도 클래스로 구성하여 HTTP 요청 기능 분리
Config와 DataLoader를 활용한 설정 및 테스트 데이터 관리
HTML Parser와 Product Parser를 통한 응답 데이터 추출 및 정규화
Response Validator와 Schema Validator를 활용한 데이터 검증
Pytest Fixture를 활용한 테스트 환경 및 클라이언트 관리
Parametrize를 활용한 검색 조건별 반복 테스트
pytest-html과 logging을 활용한 테스트 결과 관리
9. 향후 개선 방향
추가 API 엔드포인트 테스트 확장
CI/CD 기반 테스트 자동 실행
테스트 실패 시 원인 분석 및 리포트 개선