from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  pass
from constants import Embedded, Monsoon
from utils import EventHandler, b64_to_qicon


class SystemTrayViewModel():
  def __init__(self) -> None:
    self.icon = b64_to_qicon(Embedded.icon())
    self.tooltip = Monsoon.TITLE.value
    self.action_title = Monsoon.TITLE.value
    self.action_github = "GitHub"
    self.action_github_link = "https://github.com/MissUwuieTime/monsoon"
    self.action_about = "About"
    self.action_exit = "Exit"

    self.property_changed = EventHandler()