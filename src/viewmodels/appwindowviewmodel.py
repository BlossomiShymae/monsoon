from __future__ import annotations
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
  pass

from constants import Embedded, Monsoon
from utils import EventHandler, b64_to_qpixmap

from dependency_injector.wiring import Provide, inject


class AppWindowViewModel():
  @inject
  def __init__(
    self
  ):
    self.object_name = "appView"
    self.height = Monsoon.HEIGHT.value
    self.width = Monsoon.WIDTH.value
    self.wordmark_qpixmap = b64_to_qpixmap(Embedded.wordmark())

    self.property_changed = EventHandler()