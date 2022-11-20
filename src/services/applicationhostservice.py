
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from services import ExecutorService, GraphicalWorkerService
  from views import MainView, SystemTray
from constants import Stylesheet, Embedded
from templates import SystemTray
from utils import b64_to_qicon

from dependency_injector.wiring import Provide, inject
from PySide6 import QtWidgets
import time


class ApplicationHostService():
  @inject
  def __init__(self,
   executor_service: ExecutorService = Provide["executor_service"],
   graphical_worker_service: GraphicalWorkerService = Provide["graphical_worker_service"],
   application: QtWidgets.QApplication = Provide["application"],
   system_tray: SystemTray = Provide["system_tray"],
   main_view: MainView = Provide["main_view"]) -> None:
    self.executor_service = executor_service
    self.graphical_worker_service = graphical_worker_service
    self.main_view = main_view
    self.application = application
    self.system_tray = system_tray
  
  def _configure_application(self) -> None:
    """Configure our main Qt application with settings applied.
    """
    self.application.setStyleSheet(Stylesheet.value())
    self.application.setWindowIcon(b64_to_qicon(Embedded.icon()))

  async def start_async(self):
    """Starts our main application.
    """
    self._configure_application()
    self.system_tray.show()
    
    self.executor_service.exec()

  async def stop_async(self):
    """Stops our main application.
    """
    self.executor_service.is_program_exiting = True
    await self.executor_service._kill_willump()
    self.graphical_worker_service.exit()
    self.graphical_worker_service.isRunning = False
    self.graphical_worker_service.wait()
    print()
      

