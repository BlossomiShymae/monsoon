
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from services import ExecutorService, GraphicalWorkerService
  from views import MainView
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
   main_view: MainView = Provide["main_view"]) -> None:
    self.executor_service = executor_service
    self.graphical_worker_service = graphical_worker_service
    self.main_view = main_view
    self.application = application
  
  def _configure_application(self) -> None:
    """Configure our main Qt application with settings applied.
    """
    self.application.setStyleSheet(Stylesheet.value())
    self.application.setWindowIcon(b64_to_qicon(Embedded.icon()))
  
  def _create_tray(self) -> SystemTray:
    """Create our system tray with actions.

    Returns:
        SystemTray: System tray
    """
    tray = SystemTray()
    tray.show()
    
    return tray

  async def start_async(self):
    """Starts our main application.
    """
    self._configure_application()
    tray = self._create_tray()
    
    await self.executor_service.exec_event_loop()

  async def stop_async(self):
    """Stops our main application.
    """
    self.executor_service.is_program_exiting = True
    await self.executor_service._kill_willump()
    self.graphical_worker_service.exit()
    self.graphical_worker_service.isRunning = False
    self.graphical_worker_service.wait()
    print()
      

