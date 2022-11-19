from enum import Enum

class WebSocketEvent(Enum):
  """Enum that represents the operations of a WebSocket event.
  """
  CREATE = "Create"
  DELETE = "Delete"
  UPDATE = "Update"
  
  def __eq__(self, __o: object) -> bool:
    if self.__class__ is __o.__class__:
      return self == __o
    try:
      return self.value == __o.value
    except:
      pass
    try:
      if isinstance(__o, str):
        return self.value == __o
    except:
      pass
    return NotImplemented