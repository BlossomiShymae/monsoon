from __future__ import annotations
from typing import TYPE_CHECKING, Dict
if TYPE_CHECKING:
  pass
from utils import EventHandler
from models import ChampionSelectSessionModel

from PySide6.QtCore import QThread, Signal, QObject
from lcu_driver import Connector
from watchdog.observers import Observer
from watchdog.events import (
  FileSystemEventHandler, 
  FileSystemEvent, 
  EVENT_TYPE_CREATED, 
  EVENT_TYPE_DELETED
)
from enum import Enum
import time
import asyncio
import logging


class Workers(Enum):
  LOCKFILE_WATCHER = 0,
  LCU_EVENT_PROCESSOR = 1

class CommunicationPort(QObject):
  data_signal = Signal(ChampionSelectSessionModel)
  def __init__(self):
    super().__init__()

class WorkerService():
  workers_dictionary: Dict[Workers, QThread] = dict()

  def __init__(
    self
  ):
    self.workers_dictionary[Workers.LOCKFILE_WATCHER] = LockfileWatcherWorker()
    self.workers_dictionary[Workers.LCU_EVENT_PROCESSOR] = LcuEventProcessorWorker()
  
  def get(self, key: Workers) -> QThread:
    value = self.workers_dictionary.get(key)
    if value is None:
      raise Exception("Worker does not exist in worker service. Did you forget to include it? o.o")
    return value

class LcuEventProcessorWorker(QThread):
  com = CommunicationPort()
  connector = Connector()

  def __init__(self):
    QThread.__init__(self)
    self.isRunning = False
  
  @connector.ready
  async def connect(connection):
    logging.debug("lcu-driver connected ♥")
  
  @connector.close
  async def disconnect(connection):
    logging.debug("lcu-driver disconnected")

  @connector.ws.register("/lol-champ-select/v1/session", event_types=('CREATE', 'UPDATE', 'DELETE'))
  async def update(connection, event):
    LcuEventProcessorWorker.com.data_signal.emit(
      ChampionSelectSessionModel.from_websocket_event_response(event)
    )
  
  def run(self):
    self.isRunning = True
    self.connector.start()
    while self.isRunning:
      asyncio.get_running_loop().run_until_complete(asyncio.sleep(1))

class LockfileWatcherWorker(QThread):
  lockfile_create_signal = Signal()
  lockfile_delete_signal = Signal()

  def __init___(self):
    QThread.__init__(self)
    self.isRunning = False

  def run(self):
    self.isRunning = True
    event_handler = LockfileHandler()
    event_handler.lockfile_changed += self.emit_signal
    observer = Observer()
    observer.schedule(event_handler, "C:\Riot Games\League of Legends")
    observer.start()
    while self.isRunning:
      time.sleep(1)
    observer.stop()
    observer.join()
  
  def emit_signal(self, sender, args):
    if args == EVENT_TYPE_CREATED:
      self.lockfile_create_signal.emit()
    if args == EVENT_TYPE_DELETED:
      self.lockfile_delete_signal.emit()

class LockfileHandler(FileSystemEventHandler):
  def __init__(self):
    super().__init__()
    self.lockfile_changed = EventHandler()

  def on_any_event(self, event: FileSystemEvent):
    path: str = event.src_path
    if "lockfile" in path:
      if not "_" in path:
        self.lockfile_changed.invoke(self, event.event_type)