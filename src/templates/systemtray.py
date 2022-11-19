import os
import webbrowser
from PySide6 import QtWidgets
from constants import Embedded, Monsoon
from utils import b64_to_qicon
from views import AboutView

class SystemTray(QtWidgets.QSystemTrayIcon):
  def __init__(self):
    super().__init__()
    
    # Setup system tray icon
    self.setIcon(b64_to_qicon(Embedded.icon()))
    self.setToolTip(Monsoon.TITLE.value)
    self.about_dialog = AboutView()

    # Set context menu
    menu = QtWidgets.QMenu()

    # Setup context menu items
    title = menu.addAction(f"{Monsoon.TITLE.value}")
    title.setEnabled(False)
    menu.addSeparator()
    github = menu.addAction("GitHub")
    github.triggered.connect(
      lambda: self._open_web_link("https://github.com/MissUwuieTime/monsoon")
    )
    about = menu.addAction("About")
    about.triggered.connect(self._open_about)
    menu.addSeparator()
    exit = menu.addAction("Exit")
    exit.triggered.connect(self._exit_application)

    self.setContextMenu(menu)
  
  def _open_about(self):
    self.about_dialog.show()

  def _open_web_link(self, url: str):
    webbrowser.open(url)
  
  def _exit_application(self):
    os._exit(0)