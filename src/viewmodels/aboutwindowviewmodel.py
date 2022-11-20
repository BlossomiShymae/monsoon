from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  pass
from constants import Embedded, Monsoon
from utils import EventHandler, b64_to_qpixmap


class AboutWindowViewModel():
  def __init__(self) -> None:
    self.title = f"About {Monsoon.TITLE.value}"
    self.object_name = "aboutView"
    self.wordmark = b64_to_qpixmap(Embedded.wordmark())
    self.labels = [
      f"Version {Monsoon.VERSION.value}",
      f"Created by {Monsoon.AUTHOR.value}",
      f"Made with love, bees, and kitties. <3"
    ]
    self.disclaimer = Monsoon.LEGAL.value

    self.property_changed = EventHandler()