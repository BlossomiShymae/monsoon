from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from viewmodels import AboutWindowViewModel
from utils import QtContainerFactory, QtContainerLayouts
from views import QImage

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
        self.about_vbox = QtContainerFactory.create(QtContainerLayouts.VERTICAL)
        self.header_box = QtContainerFactory.create(QtContainerLayouts.STACKED)
        self.content_vbox = QtContainerFactory.create(QtContainerLayouts.VERTICAL)
        self.ok_button = QtWidgets.QPushButton("Ok")
        self.ok_button.clicked.connect(self._hide_window)

        # Set header layout
        self.header_box.layout.addWidget(QImage(self.viewmodel.wordmark_pixmap))
        self.header_box.container.setMaximumHeight(100)
        self.about_vbox.layout.addWidget(self.header_box.container)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.about_vbox.layout.addWidget(separator)

        # Set information labels
        for label in self.viewmodel.labels:
            self.content_vbox.layout.addWidget(QtWidgets.QLabel(label))

        disclaimer = QtWidgets.QLabel(self.viewmodel.disclaimer)
        disclaimer.setWordWrap(True)
        disclaimer.setContentsMargins(0, 16, 0, 16)
        disclaimer.setMinimumHeight(150)
        disclaimer.setAlignment(QtCore.Qt.AlignTop)
        self.content_vbox.layout.addWidget(disclaimer)
        self.content_vbox.layout.setAlignment(QtCore.Qt.AlignTop)

        self.about_vbox.layout.addWidget(self.content_vbox.container)
        self.about_vbox.layout.addWidget(self.ok_button)
        self.about_vbox.container.setContentsMargins(16, 16, 16, 16)
        self.setFixedSize(self.about_vbox.layout.sizeHint())
        self.setCentralWidget(self.about_vbox.container)

    def _hide_window(self):
        self.hide()
