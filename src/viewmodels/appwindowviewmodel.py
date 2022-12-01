from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from services import WorkerService

from constants import Embedded, Monsoon
from services import Workers
from utils import EventHandler, b64_to_qpixmap

from PySide6 import QtCore
from dependency_injector.wiring import Provide, inject


class AppWindowViewModel():
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
    self.wordmark_qpixmap.scaled(self.wordmark_qpixmap.size(), QtCore.Qt.KeepAspectRatio)

    self.property_changed = EventHandler()

    # Start worker threads
    lockfile_watcher_worker = worker_service.get(Workers.LOCKFILE_WATCHER)
    lockfile_watcher_worker.start()
    
