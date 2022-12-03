from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from views import AboutWindowView
  from viewmodels import SystemTrayViewModel
from constants import Embedded, Monsoon
from utils import b64_to_qicon

from PySide6 import QtWidgets
from dependency_injector.wiring import Provide, inject
import os
import webbrowser


class SystemTray(QtWidgets.QSystemTrayIcon):
  @inject
  def __init__(
    self,
    system_tray_viewmodel: SystemTrayViewModel = Provide["system_tray_viewmodel"],
    about_window_view: AboutWindowView = Provide["about_window_view"]):
    super().__init__()
    self.viewmodel = system_tray_viewmodel
    self.about_window_view = about_window_view

    # Setup system tray icon
    self.setIcon(self.viewmodel.icon)
    self.setToolTip(self.viewmodel.tooltip)

    # Set context menu
    menu = QtWidgets.QMenu()

    # Setup context menu items
    title = menu.addAction(self.viewmodel.action_title)
    title.setEnabled(False)
    menu.addSeparator()
    github = menu.addAction(self.viewmodel.action_github)
    github.triggered.connect(
      lambda: self._open_web_link(self.viewmodel.action_github_link)
    )
    about = menu.addAction(self.viewmodel.action_about)
    about.triggered.connect(self._open_about)
    menu.addSeparator()
    exit = menu.addAction(self.viewmodel.action_exit)
    exit.triggered.connect(self._exit_application)

    self.setContextMenu(menu)
  
  def _open_about(self):
    self.about_window_view.show()

  def _open_web_link(self, url: str):
    webbrowser.open(url)
  
  def _exit_application(self):
    os._exit(0)