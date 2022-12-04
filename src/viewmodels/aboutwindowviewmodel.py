from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass
from constants import Monsoon
from utils import EventHandler, ResourceHelper

from PySide6 import QtGui


class AboutWindowViewModel:
    def __init__(self) -> None:
        self.title = f"About {Monsoon.TITLE}"
        self.object_name = "aboutView"
        self.wordmark_pixmap = QtGui.QPixmap()
        self.wordmark_pixmap.loadFromData(ResourceHelper.get_resource_bytes("resources/images/wordmark.png"))
        self.labels = [
            f"Version {Monsoon.VERSION}",
            f"Created by {Monsoon.AUTHOR}",
            f"Made with love, bees, and kitties. <3"
        ]
        self.disclaimer = Monsoon.LEGAL

        self.property_changed = EventHandler()
