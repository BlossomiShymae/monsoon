from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from services import WorkerService

from constants import Embedded, Monsoon
from models import DynamicBalanceModel
from services import Workers
from utils import EventHandler, b64_to_qpixmap

from PySide6 import QtCore
from dependency_injector.wiring import Provide, inject


class AppWindowViewModel(object):
  @inject
  def __init__(
    self,
    worker_service: WorkerService = Provide["worker_service"]
  ):
    self.object_name = "appView"
    self.window_title = Monsoon.TITLE.value
    self.height = Monsoon.HEIGHT.value
    self.width = Monsoon.WIDTH.value
    self.wordmark_qpixmap = b64_to_qpixmap(Embedded.wordmark())

    self._available_champion_dynamic_balances = []
    self._team_champion_dynamic_balances = []

    self.property_changed = EventHandler()

    # Start worker threads
    lockfile_watcher_worker = worker_service.get(Workers.LOCKFILE_WATCHER)
    lockfile_watcher_worker.start()
  
  @property
  def available_champion_dynamic_balances(self):
    return self._available_champion_dynamic_balances
  
  @available_champion_dynamic_balances.setter
  def available_champion_dynamic_balances(self, value):
    self._available_champion_dynamic_balances = value
    self.property_changed.invoke(self, None)
  
  @property
  def team_champion_dynamic_balances(self):
    return self._team_champion_dynamic_balances
  
  @team_champion_dynamic_balances.setter
  def team_champion_dynamic_balances(self, value):
    self._team_champion_dynamic_balances = value
    self.property_changed.invoke(self, None)
    
