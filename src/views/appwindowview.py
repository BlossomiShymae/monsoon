from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from viewmodels import AppWindowViewModel
from constants import Monsoon
from utils import LayoutFactory

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

    # Set window properties
    self.resize(Monsoon.WIDTH.value, Monsoon.HEIGHT.value)
    self.setWindowTitle(Monsoon.TITLE.value)
    self.setCentralWidget(QtWidgets.QLabel("test"))