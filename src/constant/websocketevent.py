from enum import Enum

class WebSocketEvent(Enum):
  """Enum that represents the operations of a WebSocket event.
  """
  UPDATE = "Update"
  DELETE = "Delete"