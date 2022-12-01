from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from viewmodels import AppWindowViewModel
from constants import Monsoon
from utils import LayoutFactory, QImage, StretchTypes

from dependency_injector.wiring import Provide, inject
from PySide6 import QtWidgets, QtCore

class AppWindowView(QtWidgets.QMainWindow):
  @inject
  def __init__(
    self,
    app_window_viewmodel: AppWindowViewModel = Provide["app_window_viewmodel"]
  ):
    super().__init__()
    self.viewmodel = app_window_viewmodel
    self.setObjectName(self.viewmodel.object_name)

    # Setup the view
    self.vbox = LayoutFactory.create_vertical_proxy()
    self.title_bar = LayoutFactory.create_horizontal_proxy()
    self.content_area = LayoutFactory.create_horizontal_proxy()
    self.team_champions_panel = LayoutFactory.create_vertical_proxy()
    self.team_champions_list_box = LayoutFactory.create_vertical_proxy()
    self.available_champions_panel = LayoutFactory.create_vertical_proxy()
    self.available_champions_list_box = LayoutFactory.create_grid_proxy()

    self.title_bar.layout.addWidget(QImage(self.viewmodel.wordmark_qpixmap))
    self.title_bar.widget.setMaximumHeight(64)

    self.team_champions_panel.layout.addWidget(QtWidgets.QLabel("Team Champions"))
    for i in range(5):
      self.team_champions_list_box.layout.addWidget(self.create_champion_data_template())
    self.team_champions_list_box.widget.setSizePolicy(LayoutFactory.create_size_policy(StretchTypes.VERTICAL, 3))
    self.team_champions_panel.layout.addWidget(self.team_champions_list_box.widget)

    self.available_champions_panel.layout.addWidget(QtWidgets.QLabel("Available Champions"))
    for i in range(2):
      for j in range(5):
        self.available_champions_list_box.layout.addWidget(self.create_champion_data_template(), j+1, i+1)
    self.available_champions_list_box.widget.setSizePolicy(LayoutFactory.create_size_policy(StretchTypes.VERTICAL, 1))
    self.available_champions_panel.layout.addWidget(self.available_champions_list_box.widget)

    self.content_area.layout.addWidget(self.team_champions_panel.widget)
    self.content_area.layout.addWidget(self.available_champions_panel.widget)
    self.vbox.layout.addWidget(self.title_bar.widget)
    self.vbox.layout.addWidget(self.content_area.widget)

    # Set window properties
    self.resize(self.viewmodel.width, self.viewmodel.height)
    self.setWindowTitle(self.viewmodel.window_title)
    self.setCentralWidget(self.vbox.widget)
  
  def create_champion_data_template(self) -> QtWidgets.QWidget:
    self.champion_hbox = LayoutFactory.create_horizontal_proxy()
    self.champion_image_vbox = LayoutFactory.create_vertical_proxy()
    self.champion_textblock_vbox = LayoutFactory.create_vertical_proxy()

    self.champion_image_vbox.widget.setMaximumWidth(200)
    self.champion_textblock_vbox.layout.addWidget(QtWidgets.QLabel("test"))
    self.champion_textblock_vbox.layout.addWidget(QtWidgets.QLabel("test"))
    self.champion_textblock_vbox.layout.addWidget(QtWidgets.QLabel("test"))


    self.champion_hbox.layout.addWidget(self.champion_image_vbox.widget)
    self.champion_hbox.layout.addWidget(self.champion_textblock_vbox.widget)
    return self.champion_hbox.widget
