from typing import Optional
from utils import LayoutFactory
from views import QImage

from PySide6 import QtWidgets, QtCore, QtGui


class QChampionTemplate(QtWidgets.QWidget):
  def __init__(
    self, 
  ) -> None:
    super().__init__()

    self.champion_hbox = LayoutFactory.create_horizontal_proxy()
    self.champion_image_vbox = LayoutFactory.create_vertical_proxy()
    self.champion_textblock_vbox = LayoutFactory.create_vertical_proxy()

    self.champion_image = QImage()
    self.champion_image_label = QtWidgets.QLabel("")
    self.champion_image_vbox.widget.setMaximumWidth(200)
    self.champion_image_vbox.layout.addWidget(self.champion_image_label)
    self.champion_image_vbox.layout.addWidget(self.champion_image)

    self.champion_textblock_label = QtWidgets.QLabel("")
    self.champion_textblock_vbox.layout.addWidget(self.champion_textblock_label)

    self.champion_hbox.layout.addWidget(self.champion_image_vbox.widget)
    self.champion_hbox.layout.addWidget(self.champion_textblock_vbox.widget)

    self.setLayout(self.champion_hbox.layout)

  def clear_contents(self) -> None:
    self.set_champion_image_text("")
    self.set_champion_text("")
    self.champion_image.clear()
  
  def set_champion_image(self, pixmap: QtGui.QPixmap) -> None:
    self.champion_image.setPixmap(pixmap)

  def set_champion_image_text(self, text: str) -> None:
    self.champion_image_label.setText(text)
  
  def set_champion_text(self, text: str) -> None:
    self.champion_textblock_label.setText(text)