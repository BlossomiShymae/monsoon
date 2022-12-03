import os
import sys
from pathlib import Path


class ResourceHelper():
  @staticmethod
  def get_resource_path(relative_path: str) -> str:
    try:
      base_path = sys._MEIPASS
    except AttributeError:
      base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
  
  @staticmethod
  def get_resource_bytes(relative_path: str) -> bytes:
    return Path(ResourceHelper.get_resource_path(relative_path)).read_bytes()