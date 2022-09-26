import sys
from PySide6 import QtWidgets, QtCore, QtGui
from constant import Embedded
from service import TimerService
from view import MainView

def use_embedded_icon(app: QtWidgets.QApplication, b64_image):
  pixmap = QtGui.QPixmap()
  pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))
  icon = QtGui.QIcon(pixmap)
  app.setWindowIcon(icon)

def milliseconds_from_fps(fps: int) -> int:
  return (1 / fps) * 1000

if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  view = MainView()
  view.show()

  use_embedded_icon(app, Embedded.icon())

  # Refresh view based on update tick rate (20fps)
  update_timer = TimerService(milliseconds_from_fps(20))
  update_timer.add_slot(view.refresh)

  sys.exit(app.exec())