import pytest
from utils.data_loader import DataLoader
from utils.html_parser import HtmlParser
from utils.product_parser import ProductParser
from utils.response_validator import ResponseValidator
from utils.schema_validator import SchemaValidator

# 테스트 데이터 로드
loader = DataLoader()
search_cases = loader.get_search_cases()

@pytest.fixture
def search_response(search_client):
   """상품 검색 HTTP 응답 생성"""
   params = {
       "target": "all",
       "query": "스낵면 작은컵",
       "src_area": "late"
   }
   return search_client.get(
       "/search.ssg",
       params=params
   )

@pytest.fixture
def search_result(search_response):
   """검색 응답에서 상품 데이터 추출"""
   ResponseValidator.validate_status_code(
       search_response,
       expected_status=200
   )
   response_data = HtmlParser.extract_json(
       search_response.text
   )
   products = ProductParser.extract_products(
       response_data
   )
   return {
       "response": search_response,
       "response_data": response_data,
       "products": products
   }

@pytest.fixture(scope="module")
def schema_validator():
   """상품 JSON Schema 검증기 생성"""
   return SchemaValidator("product_schema.json")

def test_search_status_code(search_response):
   """HTTP 응답 상태 코드 검증"""
   ResponseValidator.validate_status_code(
       search_response,
       expected_status=200
   )

def test_search_response_code(search_result):
   """응답 내부 코드 검증"""
   ResponseValidator.validate_response_code(
       search_result["response_data"]
   )

def test_product_list_exists(search_result):
   """검색 상품 목록 존재 여부 검증"""
   ResponseValidator.validate_products(
       search_result["products"]
   )

def test_product_required_fields(search_result):
   """상품 필수 필드 검증"""
   for product in search_result["products"]:
       ResponseValidator.validate_product_fields(product)

def test_product_price_format(search_result):
   """상품 가격 형식 검증"""
   for product in search_result["products"]:
       price = product.get("price")
       assert price is not None
       assert str(price).isdigit(), (
           f"잘못된 상품 가격 형식: {price}"
       )

@pytest.mark.parametrize(
   "search_case",
   search_cases,
   ids=[
       case["case_name"]
       for case in search_cases
   ]
)
def test_product_keyword_match(search_case, search_client):
   """검색어와 상품명 일치 여부 검증"""
   response = search_client.get(
       "/search.ssg",
       params=search_case["request"]
   )
   ResponseValidator.validate_status_code(
       response,
       expected_status=200
   )
   response_data = HtmlParser.extract_json(
       response.text
   )
   products = ProductParser.extract_products(
       response_data
   )
   ResponseValidator.validate_products(products)
   ResponseValidator.validate_search_keyword(
       products,
       search_case["expected_keyword"]
   )

def test_product_schema(search_result, schema_validator):
   """상품 데이터 JSON Schema 검증"""
   for product in search_result["products"]:
       assert schema_validator.validate(product) is True