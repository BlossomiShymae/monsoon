import sys
import webbrowser
from PySide6 import QtWidgets
from constant import Embedded, Monsoon
from util import b64_to_qicon
from view import AboutView

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
      lambda: self.__open_web_link__("https://github.com/MissUwuieTime/monsoon")
    )
    about = menu.addAction("About")
    about.triggered.connect(self.__open_about__)
    menu.addSeparator()
    exit = menu.addAction("Exit")
    exit.triggered.connect(self.__exit_application__)

    self.setContextMenu(menu)
  
  def __open_about__(self):
    self.about_dialog.show()

  def __open_web_link__(self, url: str):
    webbrowser.open(url)
  
  def __exit_application__(self):
    sys.exit()