from controllers import LeagueClientController, EventDataController
from services import ExecutorService, ApplicationHostService, GraphicalWorkerService
from views import MainWindowView, AboutWindowView, SystemTray
from viewmodels import MainWindowViewModel, AboutWindowViewModel

from dependency_injector import containers, providers
from PySide6 import QtWidgets


class Container(containers.DeclarativeContainer):
  """Represents a container used to configure services used with dependency 
  injection.
  """

  # Controllers
  league_client_controller = providers.ThreadSafeSingleton(LeagueClientController)
  event_data_controller = providers.ThreadSafeSingleton(EventDataController)

  # Services
  executor_service = providers.ThreadSafeSingleton(ExecutorService)
  application_host_service = providers.ThreadSafeSingleton(ApplicationHostService)
  graphical_worker_service = providers.ThreadSafeSingleton(GraphicalWorkerService)

  # Views and ViewModels
  application = providers.Singleton(QtWidgets.QApplication)
  system_tray = providers.Singleton(SystemTray)
  main_window_viewmodel = providers.Singleton(MainWindowViewModel)
  main_window_view = providers.Singleton(MainWindowView)
  about_window_viewmodel = providers.Singleton(AboutWindowViewModel)
  about_window_view = providers.Singleton(AboutWindowView)