import json
from pathlib import Path
from jsonschema import Draft202012Validator

class SchemaValidatorError(Exception):
   """JSON Schema 검증 과정에서 발생하는 예외"""
   pass

class SchemaValidator:
   def __init__(self, schema_file="product_schema.json"):
       self.root_dir = Path(__file__).resolve().parents[1]
       self.schema_path = (
           self.root_dir / "schemas" / schema_file
       )
       self.schema = self._load_schema()
       Draft202012Validator.check_schema(self.schema)
       self.validator = Draft202012Validator(self.schema)
   def _load_schema(self):
       if not self.schema_path.exists():
           raise FileNotFoundError(
               f"Schema 파일을 찾을 수 없습니다: {self.schema_path}"
           )
       try:
           with open(
               self.schema_path,
               "r",
               encoding="utf-8"
           ) as file:
               return json.load(file)
       except json.JSONDecodeError as e:
           raise SchemaValidatorError(
               f"Schema JSON 형식이 올바르지 않습니다: {e}"
           ) from e
   def validate(self, data):
       errors = sorted(
           self.validator.iter_errors(data),
           key=lambda error: list(error.absolute_path)
       )
       if errors:
           error_messages = []
           for error in errors:
               field = ".".join(
                   str(path) for path in error.absolute_path
               ) or "root"
               error_messages.append(
                   f"[{field}] {error.message}"
               )
           raise SchemaValidatorError(
               "\n".join(error_messages)
           )
       return True