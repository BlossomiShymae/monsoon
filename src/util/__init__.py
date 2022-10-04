from abc import abstractmethod
from PySide6 import QtCore, QtGui, QtWidgets

def b64_to_qicon(b64_image) -> QtGui.QIcon:
    icon = QtGui.QIcon(b64_to_qpixmap(b64_image))

    return icon

def b64_to_qpixmap(b64_image) -> QtGui.QPixmap:
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))

    return pixmap

class LayoutFactory():
    """Represents a static factory that creates layout widgets in tuple formats.
    """
    @abstractmethod
    def create_grid(self):
        grid = QtWidgets.QGroupBox()
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setSpacing(0)
        grid.setLayout(grid_layout)

        return (grid, grid_layout)

    @abstractmethod
    def create_horizontal():
        hbox = QtWidgets.QGroupBox()
        hbox_layout = QtWidgets.QHBoxLayout()
        hbox_layout.setSpacing(0)
        hbox.setLayout(hbox_layout)

        return (hbox, hbox_layout)
    
    @abstractmethod
    def create_vertical(self):
        vbox = QtWidgets.QGroupBox()
        vbox_layout = QtWidgets.QVBoxLayout()
        vbox_layout.setSpacing(0)
        vbox.setLayout(vbox_layout)

        return (vbox, vbox_layout)

