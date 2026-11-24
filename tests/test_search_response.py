from utils.html_parser import HtmlParser
from utils.product_parser import ProductParser

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
   # HTML 응답 추출
   html = response.text
   # HTML 내부 JSON 추출
   response_data = HtmlParser.extract_json(html)
   # 상품 목록 추출
   products = ProductParser.extract_products(
       response_data
   )
   assert len(products) > 0
   print("추출된 상품 수:", len(products))
   for product in products:
       print(product)