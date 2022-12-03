from utils.layoutfactory import LayoutFactory, StretchTypes
from utils.eventhandler import EventHandler
from utils.qtcontainerfactory import QtContainerFactory, QtWidgetContainer, QtContainerLayouts
from utils.qthelpers import QtHelpers, QtStretches

from PySide6 import QtCore, QtGui, QtWidgets


def b64_to_qicon(b64_image) -> QtGui.QIcon:
    icon = QtGui.QIcon(b64_to_qpixmap(b64_image))

    return icon

def b64_to_qpixmap(b64_image) -> QtGui.QPixmap:
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))

    return pixmap



