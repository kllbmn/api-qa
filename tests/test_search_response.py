import pytest
from utils.html_parser import HtmlParser
from utils.product_parser import ProductParser

@pytest.mark.integration
def test_search_response(search_client):
   params = {
       "target": "all",
       "query": "스낵면 작은컵",
       "src_area": "late"
   }
   response = search_client.get(
       "/search.ssg",
       params=params
   )
   assert response.status_code == 200
   html = response.text
   response_data = HtmlParser.extract_json(html)
   products = ProductParser.extract_products(response_data)
   assert len(products) > 0
   print("추출된 상품 수:", len(products))