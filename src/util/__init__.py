from PySide6 import QtCore, QtGui

def b64_to_qicon(b64_image) -> QtGui.QIcon:
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))
    icon = QtGui.QIcon(pixmap)

    return icon