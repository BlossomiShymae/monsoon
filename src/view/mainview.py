from PySide6 import QtWidgets, QtCore
from constant import Monsoon
from controller import LeagueClientController

class MainView(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    # Set instance variables
    self.client_controller = LeagueClientController()

    # Set window properties
    self.resize(Monsoon.WIDTH.value, Monsoon.HEIGHT.value)
    self.setWindowTitle(Monsoon.TITLE.value)
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
  @QtCore.Slot()
  def refresh(self):
    if (self.client_controller.is_active()):
      (left, top, right, bottom) = self.client_controller.find()

      # Calculate window dimensions
      height = bottom - top
      width = right - left

      # Adjust view based on League client (lock onto it)
      self.setGeometry(left, top, width, height)
    pass

