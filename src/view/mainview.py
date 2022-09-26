from PySide6 import QtWidgets, QtCore
from constant import Monsoon

class MainView(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    # Set window properties
    self.resize(Monsoon.WIDTH.value, Monsoon.HEIGHT.value)
    self.setWindowTitle(Monsoon.TITLE.value)
    

