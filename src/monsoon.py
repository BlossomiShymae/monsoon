import sys
from PySide6 import QtWidgets, QtCore, QtGui
from constant import Embedded
from view import MainView

def use_embedded_icon(app: QtWidgets.QApplication, b64_image):
  pixmap = QtGui.QPixmap()
  pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))
  icon = QtGui.QIcon(pixmap)
  app.setWindowIcon(icon)

if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  view = MainView()
  view.show()

  use_embedded_icon(app, Embedded.icon())

  sys.exit(app.exec())