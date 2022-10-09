from typing import Tuple
from PySide6 import QtWidgets

class LayoutFactory():
    """Represents a static factory that creates layout widgets in tuple formats.
    """
    @staticmethod
    def create_grid() -> Tuple[QtWidgets.QGroupBox, QtWidgets.QGridLayout]:
        grid = QtWidgets.QGroupBox()
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setSpacing(0)
        grid.setLayout(grid_layout)

        return (grid, grid_layout)

    @staticmethod
    def create_horizontal() -> Tuple[QtWidgets.QGroupBox, QtWidgets.QHBoxLayout]:
        hbox = QtWidgets.QGroupBox()
        hbox_layout = QtWidgets.QHBoxLayout()
        hbox_layout.setSpacing(0)
        hbox.setLayout(hbox_layout)

        return (hbox, hbox_layout)
    
    @staticmethod
    def create_vertical() -> Tuple[QtWidgets.QGroupBox, QtWidgets.QVBoxLayout]:
        vbox = QtWidgets.QGroupBox()
        vbox_layout = QtWidgets.QVBoxLayout()
        vbox_layout.setSpacing(0)
        vbox.setLayout(vbox_layout)

        return (vbox, vbox_layout)