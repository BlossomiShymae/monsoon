from PySide6 import QtWidgets, QtCore, QtGui

class QImage(QtWidgets.QLabel):
  def __init__(self, pixmap: QtGui.QPixmap = None, parent=None):
    super().__init__(parent)
    self.setScaledContents(True)
    if pixmap is not None:
      self.setPixmap(pixmap)

  def hasHeightForWidth(self) -> bool:
    return self.pixmap() is not None

  def heightForWidth(self, w: int) -> int:
    if self.pixmap():
      return int(w * (self.pixmap().height() / self.pixmap().width()))
    return 0
  
  def paintEvent(self, event: QtGui.QPaintEvent) -> None:
    if self.pixmap():
      size = self.size()
      painter = QtGui.QPainter(self)
      point = QtCore.QPoint(0,0)
      scaledPix = self.pixmap().scaled(size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
      point.setX(0)
      point.setY(0)
      painter.drawPixmap(point, scaledPix)
      self.setMaximumSize(QtCore.QSize(4000,5000))