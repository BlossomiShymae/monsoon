import os
import sys
sys.path.append(os.path.abspath("./src/"))

from services import WorkerService
from views import AppWindowView
from viewmodels import AppWindowViewModel
from PySide6 import QtWidgets

app = QtWidgets.QApplication()
worker_service = WorkerService()
app_window_viewmodel = AppWindowViewModel(worker_service=worker_service)
app_window_view = AppWindowView(app_window_viewmodel=app_window_viewmodel)

app_window_view.show()
try:
  app.exec()
except KeyboardInterrupt:
  sys.exit(0)