from utils.api_client import APIClient
from utils.config import Config

def test_search_page_connection(search_client):
   params = {
       "target": "all",
       "query": "스낵면 소컵",
       "src_area": "late"
   }
   response = search_client.get(
       "/search.ssg",
       params=params
   )
   assert response.status_code == 200
   content_type = response.headers.get("Content-Type", "")
   assert "text/html" in content_type
   assert len(response.text) > 0