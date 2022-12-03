from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from views import AppWindowView, SystemTray
from utils import ResourceHelper

from dependency_injector.wiring import Provide, inject
from PySide6 import QtWidgets, QtGui
import os
import traceback
import qdarktheme


class ApplicationHostService():
  @inject
  def __init__(
   self,
   application: QtWidgets.QApplication = Provide["application"],
   system_tray: SystemTray = Provide["system_tray"],
   app_window_view: AppWindowView = Provide["app_window_view"]
  ) -> None:
    self.app_window_view = app_window_view
    self.application = application
    self.system_tray = system_tray
  
  def _configure_application(self) -> None:
    """Configure our main Qt application with settings applied.
    """
    self.application.setStyleSheet(qdarktheme.load_stylesheet())
    icon_pixmap = QtGui.QPixmap()
    icon_pixmap.loadFromData(ResourceHelper.get_resource_bytes("resources/images/monsoon.ico"))
    self.application.setWindowIcon(icon_pixmap)

  def start(self):
    """Starts our main application.
    """
    self._configure_application()
    self.system_tray.show()
    self.app_window_view.show()
    
    try:
      self.application.exec()
      self.stop()
    except Exception:
      self.on_exception()

  def stop(self):
    """Stops our main application.
    """
    os._exit(0)
  
  def on_exception(self):
    """Prepare to gracefully exit program.
    """
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(traceback.format_exc())
    msg.setWindowTitle(":bee_sad:")
    msg.exec_()
    self.stop()

