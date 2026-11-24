import pytest
from utils.data_loader import DataLoader
from utils.html_parser import HtmlParser
from utils.product_parser import ProductParser
from utils.response_validator import ResponseValidator

# Negative 테스트 데이터 로드
loader = DataLoader()
negative_cases = loader.load_json(
   "negative_cases.json"
)["negative_cases"]

@pytest.mark.integration
@pytest.mark.parametrize(
   "test_case",
   negative_cases,
   ids=[
       case["case_name"]
       for case in negative_cases
   ]
)
def test_negative_product_search(test_case, search_client):
   """비정상 검색 조건에 대한 상품 검색 결과 검증"""
   # 1. 검색 요청
   response = search_client.get(
       "/search.ssg",
       params=test_case["request"]
   )
   # 2. HTTP 상태 코드 검증
   ResponseValidator.validate_status_code(
       response,
       expected_status=200
   )
   # 3. HTML 내부 JSON 데이터 추출
   response_data = HtmlParser.extract_json(
       response.text
   )
   # 4. 검색 결과 상품 추출
   products = ProductParser.extract_products(
       response_data
   )
   # 5. 기대 상품 수와 실제 상품 수 비교
   expected_count = test_case["expected_product_count"]
   assert len(products) == expected_count, (
       f"상품 개수 불일치: "
       f"기대값={expected_count}, "
       f"실제값={len(products)}"
   )
   print(
       f"\n[{test_case['case_name']}] "
       f"추출 상품 수: {len(products)}"
   )