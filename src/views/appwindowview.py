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
    self.available_champions_list_box = LayoutFactory.create_horizontal_proxy()
    self.team_champions_list_box = LayoutFactory.create_horizontal_proxy()

    self.title_bar.layout.addWidget(QImage(self.viewmodel.wordmark_qpixmap))
    self.title_bar.widget.setMaximumHeight(64)

    self.available_champions_list_box.widget.setSizePolicy(LayoutFactory.create_size_policy(StretchTypes.VERTICAL, 1))
    self.team_champions_list_box.widget.setSizePolicy(LayoutFactory.create_size_policy(StretchTypes.VERTICAL, 3))

    self.vbox.layout.addWidget(self.title_bar.widget)
    self.vbox.layout.addWidget(self.available_champions_list_box.widget)
    self.vbox.layout.addWidget(self.team_champions_list_box.widget)

    # Set window properties
    self.resize(self.viewmodel.width, self.viewmodel.height)
    self.setWindowTitle(self.viewmodel.window_title)
    self.setCentralWidget(self.vbox.widget)