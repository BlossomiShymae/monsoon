from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from controllers import EventDataController, LeagueClientController
from utils import milliseconds_from_fps

from PySide6.QtCore import QThread, Signal
from dependency_injector.wiring import Provide, inject
import time


class GraphicalWorkerService(QThread):
  update_signal = Signal(bool)
  @inject
  def __init__(
    self, 
    league_client_controller: LeagueClientController = Provide["league_client_controller"],
    event_data_controller: EventDataController = Provide["event_data_controller"]
  ):
    QThread.__init__(self)
    self.league_client_controller = league_client_controller
    self.event_data_controller = event_data_controller
    self.isRunning = False
  
  def run(self):
    self.isRunning = True
    while self.isRunning:
      self.update_signal.emit(True)
      time.sleep(milliseconds_from_fps(20) / 1000)

