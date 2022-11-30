from __future__ import annotations
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
  from controllers import EventDataController, LeagueClientController
  from services import ExecutorService, GraphicalWorkerService

from constants import Embedded
from models import BalanceModel
from utils import EventHandler, b64_to_qpixmap

from dependency_injector.wiring import Provide, inject


class MainWindowViewModel():
  @inject
  def __init__(
    self,
    executor_service: ExecutorService = Provide["executor_service"],
    graphical_worker_service: GraphicalWorkerService = Provide["graphical_worker_service"],
    event_data_controller: EventDataController = Provide["event_data_controller"],
    league_client_controller: LeagueClientController = Provide["league_client_controller"]
  ):
    self.executor_service = executor_service
    self.graphical_worker_service = graphical_worker_service
    self.event_data_controller = event_data_controller
    self.league_client_controller = league_client_controller
    
    self.object_name = "mainView"
    self.height = 0
    self.width = 0
    self.left = 0
    self.top = 0
    self.wordmark = b64_to_qpixmap(Embedded.wordmark())
    self.is_league_client_active = False
    self.is_session_active = False
    self.is_client_foreground = False
    self.is_client_overlayed = False
    self.team_balances: List[str] = []
    self.team_other_balances: List[str] = []
    self.bench_balances: List[str] = []

    self.property_changed = EventHandler()
    self.graphical_worker_service.update_signal.connect(self.update_properties)
    self.graphical_worker_service.start()
    
  def update_properties(self):
    if self.league_client_controller.find() != None:
      (left, top, right, bottom) = self.league_client_controller.find()
      self.left = left
      self.top = top
      # Calculate window dimensions
      self.height = bottom - top
      self.width = right - left
    
    (self.is_session_active,
     self.team_balances,
      self.team_other_balances,
       self.bench_balances) = self.event_data_controller.get_state()
    self.is_league_client_active = self.league_client_controller.is_active()
    self.is_client_foreground = self.league_client_controller.is_foreground()
    self.is_client_overlayed = self.league_client_controller.is_overlayed()
    self.property_changed.invoke(sender=self, event_args=None)
      

