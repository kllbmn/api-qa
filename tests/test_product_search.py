import pytest

from utils.response_validator import ResponseValidator
from utils.schema_validator import SchemaValidator
from utils.html_parser import HtmlParser
from utils.product_parser import ProductParser


@pytest.fixture
def sample_product():
   """상품 데이터 검증에 사용할 테스트 데이터"""
   return {
       "item_id": "1000628999266",
       "item_name": "오뚜기 스낵면 작은컵 6입",
       "site_no": "6004",
       "salestr_no": "6005",
       "price": "9700",
       "price_text": "9,700원",
       "sold_out": "N",
       "stopped_selling": "N",
       "item_url": "https://qa-mall.shinsegae.com/item/itemView.ssg",
       "image_url": "https://qa-sitem.shinsegaecdn.com/item.jpg"
   }


@pytest.fixture
def schema_validator():
   """상품 JSON Schema 검증기 생성"""
   return SchemaValidator("product_schema.json")


# ==============================
# 정상 테스트 (Unit Test)
# ==============================

def test_search_response_code():
   response_data = {"res_code": "200"}

   ResponseValidator.validate_response_code(response_data)


def test_product_list_exists(sample_product):
   ResponseValidator.validate_products([sample_product])


def test_product_required_fields(sample_product):
   ResponseValidator.validate_product_fields(sample_product)


def test_product_price_format(sample_product):
   ResponseValidator.validate_product_fields(sample_product)


def test_product_schema(sample_product, schema_validator):
   assert schema_validator.validate(sample_product) is True


# ==============================
# 부정 테스트 (Unit Test)
# ==============================

def test_product_name_missing(sample_product):
   invalid_product = sample_product.copy()
   invalid_product["item_name"] = ""

   with pytest.raises(AssertionError):
       ResponseValidator.validate_product_fields(invalid_product)


def test_product_id_missing(sample_product):
   invalid_product = sample_product.copy()
   invalid_product["item_id"] = None

   with pytest.raises(AssertionError):
       ResponseValidator.validate_product_fields(invalid_product)


def test_product_invalid_price(sample_product):
   invalid_product = sample_product.copy()
   invalid_product["price"] = "12A"

   with pytest.raises(AssertionError):
       ResponseValidator.validate_product_fields(invalid_product)


def test_product_negative_price(sample_product):
   invalid_product = sample_product.copy()
   invalid_product["price"] = "-100"

   with pytest.raises(AssertionError):
       ResponseValidator.validate_product_fields(invalid_product)


def test_empty_product_list():
   with pytest.raises(AssertionError):
       ResponseValidator.validate_products([])


# ==============================
# Integration Test
# ==============================

@pytest.mark.integration
def test_search_status_code(search_client):
   params = {
       "target": "all",
       "query": "스낵면 작은컵",
       "src_area": "late"
   }

   response = search_client.get(
       "/search.ssg",
       params=params
   )

   ResponseValidator.validate_status_code(
       response,
       expected_status=200
   )


@pytest.mark.integration
@pytest.mark.parametrize(
   "search_case",
   [
       {
           "case_name": "스낵면 작은컵 검색",
           "request": {
               "target": "all",
               "query": "스낵면 작은컵",
               "src_area": "late"
           },
           "expected_keyword": "스낵면 작은컵"
       },
       {
           "case_name": "스낵면 검색",
           "request": {
               "target": "all",
               "query": "스낵면",
               "src_area": "late"
           },
           "expected_keyword": "스낵면"
       },
       {
           "case_name": "라면 검색",
           "request": {
               "target": "all",
               "query": "라면",
               "src_area": "late"
           },
           "expected_keyword": "라면"
       }
   ],
   ids=lambda case: case["case_name"]
)
def test_product_keyword_match(search_case, search_client):
   response = search_client.get(
       "/search.ssg",
       params=search_case["request"]
   )

   ResponseValidator.validate_status_code(
       response,
       expected_status=200
   )

   response_data = HtmlParser.extract_json(response.text)
   products = ProductParser.extract_products(response_data)

   ResponseValidator.validate_products(products)

   ResponseValidator.validate_search_keyword(
       products,
       search_case["expected_keyword"]
   )