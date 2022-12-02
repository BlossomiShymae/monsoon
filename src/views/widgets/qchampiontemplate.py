from typing import List
from utils import LayoutFactory, StretchTypes, clear_qlayout
from views import QImage

from PySide6 import QtWidgets, QtCore, QtGui


class QChampionTemplate(QtWidgets.QWidget):
  def __init__(
    self, 
  ) -> None:
    super().__init__()

    self.champion_hbox = LayoutFactory.create_horizontal_proxy()
    self.champion_image_vbox = LayoutFactory.create_vertical_proxy()
    self.champion_content_hbox = LayoutFactory.create_horizontal_proxy()
    self.champion_modifiers_vbox = LayoutFactory.create_vertical_proxy()
    self.champion_modifiers_list_box = LayoutFactory.create_vertical_proxy()

    self.champion_image = QImage()
    self.champion_image_box = LayoutFactory.create_horizontal_proxy()
    self.champion_image_box.widget.setMaximumHeight(80)
    self.champion_image_box.widget.setMaximumWidth(80)
    self.champion_image_box.layout.addWidget(self.champion_image)
    self.champion_image_label = QtWidgets.QLabel("")
    self.champion_image_vbox.layout.setAlignment(QtCore.Qt.AlignTop)
    self.champion_image_vbox.layout.addWidget(self.champion_image_box.widget)
    self.champion_image_vbox.layout.addWidget(self.champion_image_label)

    self.champion_modifiers_label = QtWidgets.QLabel("Modifiers")
    self.champion_modifiers_label.setStyleSheet("""
    QWidget {
      font-size: 12pt;
      font-weight: 400;
    }
    """)
    self.champion_modifiers_vbox.layout.setAlignment(QtCore.Qt.AlignTop)
    self.champion_modifiers_vbox.layout.addWidget(self.champion_modifiers_label)
    self.champion_modifiers_vbox.layout.addWidget(self.champion_modifiers_list_box.widget)
    self.champion_content_hbox.widget.setSizePolicy(
      LayoutFactory.create_size_policy(StretchTypes.HORIZONTAL, 1)
    )
    self.champion_content_hbox.layout.setAlignment(QtCore.Qt.AlignTop)
    self.champion_content_hbox.layout.addWidget(self.champion_modifiers_vbox.widget)

    self.champion_hbox.layout.addWidget(self.champion_image_vbox.widget)
    self.champion_hbox.layout.addWidget(self.champion_content_hbox.widget)

    self.setLayout(self.champion_hbox.layout)
    self.setStyleSheet("background-color: #103038;")

  def clear_contents(self) -> None:
    self.set_champion_image_text("")
    clear_qlayout(self.champion_modifiers_list_box.layout)
    self.champion_image.clear()
  
  def set_champion_image(self, pixmap: QtGui.QPixmap) -> None:
    self.champion_image.setPixmap(pixmap)

  def set_champion_image_text(self, text: str) -> None:
    self.champion_image_label.setText(text)

  def set_champion_image_text_stylesheet(self, stylesheet: str) -> None:
    self.champion_image_label.setStyleSheet(stylesheet)
  
  def set_champion_modifiers_data_source(self, data: List[str]) -> None:
    for modifier_string in data:
      label = QtWidgets.QLabel(modifier_string)
      label.setStyleSheet("""
      QWidget {
        font-size: 8pt;
        font-weight: 600;
      }
      """)
      self.champion_modifiers_list_box.layout.addWidget(label)
  
  def set_champion_modifiers_stylesheet(self, stylesheet: str) -> None:
    self.champion_textblock_label.setStyleSheet(stylesheet)