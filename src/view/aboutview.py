from PySide6 import QtWidgets, QtCore
from constant import Embedded, Monsoon
from util import b64_to_qpixmap, LayoutFactory

class AboutView(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    # Set window properties
    self.setWindowTitle(f"About {Monsoon.TITLE.value}")
    self.setObjectName("aboutView")

    # Set instance variables
    (self.vbox, self.vbox_layout) = LayoutFactory.create_vertical()
    (self.header, self.header_layout) = LayoutFactory.create_horizontal()
    self.ok_button = QtWidgets.QPushButton("Ok")
    self.ok_button.clicked.connect(self.__close_window__)

    # Set header layout
    wordmark_label = QtWidgets.QLabel("")
    wordmark_label.setPixmap(b64_to_qpixmap(Embedded.wordmark()))
    self.header_layout.addWidget(wordmark_label);
    self.header_layout.setAlignment(QtCore.Qt.AlignCenter)
    self.vbox_layout.addWidget(self.header)

    separator = QtWidgets.QFrame()
    separator.setFrameShape(QtWidgets.QFrame.HLine)
    separator.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.vbox_layout.addWidget(separator)

    # Set information labels
    self.vbox_layout.addWidget(QtWidgets.QLabel(f"Version {Monsoon.VERSION.value}"))
    self.vbox_layout.addWidget(QtWidgets.QLabel(f"Created by {Monsoon.AUTHOR.value}"))
    self.vbox_layout.addWidget(QtWidgets.QLabel("Made with love, bees, and kitties. <3"))

    disclaimer = QtWidgets.QLabel(Monsoon.LEGAL.value)
    disclaimer.setWordWrap(True)
    disclaimer.setContentsMargins(0, 16, 0, 16)
    self.vbox_layout.addWidget(disclaimer)
    self.vbox_layout.addWidget(self.ok_button)

    self.vbox_layout.setSpacing(2)
    self.setFixedSize(self.vbox_layout.sizeHint())
    self.setCentralWidget(self.vbox)

  def __close_window__(self):
    self.close()

