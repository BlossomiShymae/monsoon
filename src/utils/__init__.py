from utils.layoutfactory import LayoutFactory, StretchTypes
from utils.eventhandler import EventHandler
from utils.widgets import QImage

from PySide6 import QtCore, QtGui


class Timer():
  def __init__(self, interval=int):
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.update)
    self.timer.start(interval)

  def add_slot(self, slot):
    self.timer.timeout.connect(slot)

  @QtCore.Slot()
  def update(self):
    pass

def b64_to_qicon(b64_image) -> QtGui.QIcon:
    icon = QtGui.QIcon(b64_to_qpixmap(b64_image))

    return icon

def b64_to_qpixmap(b64_image) -> QtGui.QPixmap:
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))

    return pixmap

def milliseconds_from_fps(fps: int) -> int:
  """Calculate milliseconds from the rate of frames per second.

  Args:
      fps (int): Frames per second

  Returns:
      int: Milliseconds
  """
  return (1 / fps) * 1000



