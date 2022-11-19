from controllers import LeagueClientController, EventDataController
from services import ExecutorService, ApplicationHostService
from views import MainView

from dependency_injector import containers, providers
from PySide6 import QtWidgets

class Container(containers.DeclarativeContainer):
  """Represents a container used to configure services used with dependency 
  injection.
  """

  # Controllers
  league_client_controller = providers.Singleton(LeagueClientController)
  event_data_controller = providers.Singleton(EventDataController)

  # Services
  executor_service = providers.ThreadSafeSingleton(ExecutorService)
  application_host_service = providers.ThreadSafeSingleton(ApplicationHostService)

  # Views
  application = providers.Singleton(QtWidgets.QApplication)
  main_view = providers.Singleton(MainView)