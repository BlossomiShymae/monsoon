from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  pass
from constants import Embedded, Monsoon
from utils import EventHandler, ResourceHelper

from PySide6 import QtGui

class SystemTrayViewModel():
  def __init__(self) -> None:
    self.icon_pixmap = QtGui.QPixmap()
    self.icon_pixmap.loadFromData(ResourceHelper.get_resource_bytes("resources/images/monsoon.ico"))
    self.tooltip = Monsoon.TITLE.value
    self.action_title = Monsoon.TITLE.value
    self.action_github = "GitHub"
    self.action_github_link = "https://github.com/MissUwuieTime/monsoon"
    self.action_about = "About"
    self.action_exit = "Exit"

    self.property_changed = EventHandler()