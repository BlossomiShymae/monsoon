from PySide6 import QtCore, QtGui, QtWidgets
from constant import Embedded, Monsoon

class SystemTray(QtWidgets.QSystemTrayIcon):
  def __init__(self):
    super().__init__()
    self.setIcon(self.__b64_to_qicon(Embedded.icon()))
    self.setToolTip(Monsoon.TITLE.value)

    # Set context menu
    menu = QtWidgets.QMenu()

    title = menu.addAction(f"{Monsoon.TITLE.value}")
    title.setEnabled(False)
    menu.addSeparator()
    github = menu.addAction("GitHub")
    menu.addSeparator()
    exit = menu.addAction("Exit")

    self.setContextMenu(menu)

  def __b64_to_qicon(self, b64_image) -> QtGui.QIcon:
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))
    icon = QtGui.QIcon(pixmap)

    return icon