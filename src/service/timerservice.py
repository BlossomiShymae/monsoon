from PySide6 import QtCore

class TimerService():
  def __init__(self, interval=int):
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.update)
    self.timer.start(interval)

  def add_slot(self, slot):
    self.timer.timeout.connect(slot)

  @QtCore.Slot()
  def update(self):
    pass