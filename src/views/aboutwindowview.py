from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.viewmodels import AboutWindowViewModel
from src.utils import LayoutFactory

from PySide6 import QtWidgets, QtCore
from dependency_injector.wiring import Provide, inject


class AboutWindowView(QtWidgets.QMainWindow):
    @inject
    def __init__(
            self,
            about_window_viewmodel: AboutWindowViewModel = Provide["about_window_viewmodel"]
    ):
        super().__init__()
        self.viewmodel = about_window_viewmodel
        # Set window properties
        self.setWindowTitle(self.viewmodel.title)
        self.setObjectName(self.viewmodel.object_name)

        # Set instance variables
        (self.vbox, self.vbox_layout) = LayoutFactory.create_vertical()
        (self.header, self.header_layout) = LayoutFactory.create_horizontal()
        self.ok_button = QtWidgets.QPushButton("Ok")
        self.ok_button.clicked.connect(self._hide_window)

        # Set header layout
        wordmark_label = QtWidgets.QLabel("")
        wordmark_label.setPixmap(self.viewmodel.wordmark_pixmap)
        self.header_layout.addWidget(wordmark_label);
        self.header_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox_layout.addWidget(self.header)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vbox_layout.addWidget(separator)

        # Set information labels
        for label in self.viewmodel.labels:
            self.vbox_layout.addWidget(QtWidgets.QLabel(label))

        disclaimer = QtWidgets.QLabel(self.viewmodel.disclaimer)
        disclaimer.setWordWrap(True)
        disclaimer.setContentsMargins(0, 16, 0, 16)
        self.vbox_layout.addWidget(disclaimer)
        self.vbox_layout.addWidget(self.ok_button)

        self.vbox_layout.setSpacing(2)
        self.setFixedSize(self.vbox_layout.sizeHint())
        self.setCentralWidget(self.vbox)

    def _hide_window(self):
        self.hide()
