import json
from pathlib import Path

class Config:
   def __init__(self, env="qa"):
       self.root_dir = Path(__file__).resolve().parents[1]
       self.config_dir = self.root_dir / "config"
       common_path = self.config_dir / "config.json"
       env_path = self.config_dir / "environments" / f"{env}.json"
       if not common_path.exists():
           raise FileNotFoundError(
               f"공통 설정 파일을 찾을 수 없습니다: {common_path}"
           )
       if not env_path.exists():
           raise FileNotFoundError(
               f"환경 설정 파일을 찾을 수 없습니다: {env_path}"
           )
       self.data = self._load_json(common_path)
       env_data = self._load_json(env_path)
       self._deep_merge(self.data, env_data)
       required_urls = [
           "search_base_url",
           "product_api_base_url"
       ]
       for key in required_urls:
           if not self.data.get(key):
               raise ValueError(f"{key} 설정이 필요합니다.")
           
   # JSON 파일 읽기
   @staticmethod
   def _load_json(path):
       with open(path, "r", encoding="utf-8") as file:
           return json.load(file)
   # 중첩된 설정 병합
   @staticmethod
   def _deep_merge(base, override):
       for key, value in override.items():
           if (
               key in base
               and isinstance(base[key], dict)
               and isinstance(value, dict)
           ):
               Config._deep_merge(base[key], value)
           else:
               base[key] = value
   # 설정값 조회
   def get(self, *keys, default=None):
       value = self.data
       for key in keys:
           if not isinstance(value, dict) or key not in value:
               return default
           value = value[key]
       return value