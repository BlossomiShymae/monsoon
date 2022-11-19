
from constants import Stylesheet, Embedded
from services import ExecutorService
from templates import SystemTray
from utils import Timer, b64_to_qicon, milliseconds_from_fps
from views import MainView

from dependency_injector.wiring import Provide, inject
from PySide6 import QtWidgets


class ApplicationHostService():
  @inject
  def __init__(self,
   executor_service: ExecutorService = Provide["executor_service"],
   application: QtWidgets.QApplication = Provide["application"],
   main_view: MainView = Provide["main_view"]) -> None:
    self.executor_service = executor_service
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
    
    update_timer = Timer(milliseconds_from_fps(20))
    update_timer.add_slot(self.main_view.refresh)
    await self.executor_service.exec_event_loop()

  async def stop_async(self):
    """Stops our main application.
    """
    self.executor_service.is_program_exiting = True
    await self.executor_service._kill_willump()
    print()
      

