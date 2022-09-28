from enum import Enum

class WebSocketEvent(Enum):
  """Enum that represents the operations of a WebSocket event.
  """
  CREATE = "Create"
  DELETE = "Delete"
  UPDATE = "Update"
  