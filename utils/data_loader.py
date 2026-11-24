import json
from pathlib import Path

class DataLoader:
   def __init__(self):
       self.root_dir = Path(__file__).resolve().parents[1]
       self.data_dir = self.root_dir / "test_data"
   def load_json(self, file_name):
       file_path = self.data_dir / file_name
       if not file_path.exists():
           raise FileNotFoundError(
               f"테스트 데이터 파일을 찾을 수 없습니다: {file_path}"
           )
       try:
           with open(file_path, "r", encoding="utf-8") as file:
               return json.load(file)
       except json.JSONDecodeError as e:
           raise ValueError(
               f"JSON 파일 형식이 올바르지 않습니다: {file_name}"
           ) from e
   def get_search_cases(self):
       data = self.load_json("products.json")
       search_cases = data.get("search_cases")
       if not isinstance(search_cases, list):
           raise ValueError(
               "search_cases는 리스트 형식이어야 합니다."
           )
       return search_cases