import json

class HtmlParserError(Exception):
   """HTML 파싱 과정에서 발생하는 예외"""
   pass

class HtmlParser:
   @staticmethod
   def extract_json(html):
       if not isinstance(html, str) or not html:
           raise HtmlParserError("HTML 응답이 비어 있습니다.")
       marker = "ITEM_UNIT_LIST"
       marker_index = html.find(marker)
       if marker_index == -1:
           raise HtmlParserError(
               "HTML에서 ITEM_UNIT_LIST를 찾을 수 없습니다."
           )
       decoder = json.JSONDecoder()
       # ITEM_UNIT_LIST 이전에 있는 JSON 객체 시작 위치 탐색
       start_positions = [
           index for index, char in enumerate(html[:marker_index])
           if char == "{"
       ]
       for start in reversed(start_positions):
           try:
               data, _ = decoder.raw_decode(html, start)
               if not isinstance(data, dict):
                   continue
               response_data = data.get("data")
               if not isinstance(response_data, dict):
                   continue
               data_list = response_data.get("dataList")
               if not isinstance(data_list, list):
                   continue
               has_product_unit = any(
                   isinstance(unit, dict)
                   and unit.get("unitType") == marker
                   for unit in data_list
               )
               if has_product_unit:
                   return data
           except json.JSONDecodeError:
               continue
       raise HtmlParserError(
           "상품 목록이 포함된 JSON 응답 객체를 찾지 못했습니다."
       )