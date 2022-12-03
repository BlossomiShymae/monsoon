from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from services import WorkerService, ApiService

from constants import Embedded, Monsoon
from models import DynamicBalanceModel, ChampionSelectSessionModel
from services import Workers
from utils import EventHandler, ResourceHelper

from PySide6 import QtCore, QtGui
from dependency_injector.wiring import Provide, inject
import logging


class AppWindowViewModel(object):
  @inject
  def __init__(
    self,
    worker_service: WorkerService = Provide["worker_service"],
    api_service: ApiService = Provide["api_service"]
  ):
    self.object_name = "appView"
    self.window_title = Monsoon.TITLE.value
    self.height = Monsoon.HEIGHT.value
    self.width = Monsoon.WIDTH.value
    self.wordmark_pixmap = QtGui.QPixmap()
    self.wordmark_pixmap.loadFromData(ResourceHelper.get_resource_bytes("resources/images/wordmark.png"))

    self._available_champion_dynamic_balances = []
    self._team_champion_dynamic_balances = []
    self._is_enabled = False

    self.property_changed = EventHandler()

    self.api_service = api_service
    # Start worker threads
    lockfile_watcher_worker = worker_service.get(Workers.LOCKFILE_WATCHER)
    lockfile_watcher_worker.start()
    lcu_event_processor_worker = worker_service.get(Workers.LCU_EVENT_PROCESSOR)
    lcu_event_processor_worker.com.data_signal.connect(self.on_data)
    lcu_event_processor_worker.start()

  @QtCore.Slot(ChampionSelectSessionModel)
  def on_data(self, data: ChampionSelectSessionModel):
    team_champion_dynamic_balances = []
    for id in data.team_champion_ids:
      champion = self.api_service.data_dragon.fetch_by_champion_id(id)
      balance = self.api_service.lol_fandom.fetch_dynamic_balance_by_champion_name(champion["name"])
      balance.champion_icon = self.api_service.data_dragon.fetch_icon_by_champion_id(id)
      team_champion_dynamic_balances.append(balance)
    available_champion_dynamic_balances = []
    for id in data.available_champion_ids:
      champion = self.api_service.data_dragon.fetch_by_champion_id(id)
      balance = self.api_service.lol_fandom.fetch_dynamic_balance_by_champion_name(champion["name"])
      balance.champion_icon = self.api_service.data_dragon.fetch_icon_by_champion_id(id)
      available_champion_dynamic_balances.append(balance)
    
    self.team_champion_dynamic_balances = team_champion_dynamic_balances
    self.available_champion_dynamic_balances = available_champion_dynamic_balances

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
  
  @property
  def is_enabled(self):
    return self._is_enabled
  
  @is_enabled.setter
  def is_enabled(self, value):
    self._is_enabled = value
    self.property_changed.invoke(self, None)
