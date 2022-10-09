from util.layoutfactory import LayoutFactory

from PySide6 import QtCore, QtGui

def b64_to_qicon(b64_image) -> QtGui.QIcon:
    icon = QtGui.QIcon(b64_to_qpixmap(b64_image))

    return icon

def b64_to_qpixmap(b64_image) -> QtGui.QPixmap:
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))

    return pixmap



