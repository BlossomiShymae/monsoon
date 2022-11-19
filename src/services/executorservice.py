from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from controllers import EventDataController, LeagueClientController
from utils import EventHandler

import asyncio
from dependency_injector.wiring import Provide, inject
import logging
import json
from PySide6 import QtWidgets
from threading import Thread
from time import sleep
import willump


class ExecutorService():
  """Represents the executor that manages the state of the program.
  """
  @inject
  def __init__(
    self, 
    application: QtWidgets.QApplication = Provide["application"],
    league_client_controller: LeagueClientController = Provide["league_client_controller"],
    event_data_controller: EventDataController = Provide["event_data_controller"]):
    self.application = application
    self.league_client_controller = league_client_controller
    self.event_data_controller = event_data_controller
    self.is_program_exiting = False
    self.is_willump_active = False
    self.subscription = None
    self.ui_event_loop = asyncio.get_event_loop()
    self.wllp = None


  async def _on_websocket_event(self, data):
    """Pass WebSocket event data to the event data controller. Mutative.

    Args:
        data (object): League client event data
    """
    print(json.dumps(data, indent=4, sort_keys=True))
    self.event_data_controller.events_queue.append(data)
  
  async def _kill_willump(self):
    """Attempt to close willump asynchronosuly. Mutative.
    """
    try:
      await self.wllp.close()
    except Exception:
      pass
    finally:
      self.wllp = None
      self.is_willump_active = False

  async def _exec_willump(self):
    """Execute willump asynchronously with WebSocket subscription. Mutative.
    """
    self.wllp = await willump.start()
    # Sleep for five seconds to ensure that the WebSocket subscription works. u.u
    # This should be handled by `willump` but we have to bandaid fix this for now. :c
    # Submit a pull request if a better alternative is found.
    sleep(5)
    self.subscription = await self.wllp.subscribe(
      "OnJsonApiEvent_lol-champ-select_v1_session",
        default_handler=self._on_websocket_event
    )

  def _process(self):
    """Process the state of willump and create appropriate futures in event loop.
    """
    asyncio.set_event_loop(loop=self.ui_event_loop)
    if self.league_client_controller.is_active():
      if self.is_willump_active:
        logging.debug("hugging willump... :3")
        return

      logging.debug("requesting willump... o.o")
      self.is_willump_active = True
      asyncio.ensure_future(self._exec_willump())
      return

    # Probable that the League client process is dead if we have reached this point.
    logging.debug("bye bye willump... u.u")
    asyncio.ensure_future(self._kill_willump())


  def _exec_client_loop_task(self):
    """Long-running client processing loop that will run in a seperate thread.
    """
    while True:
      if self.is_program_exiting:
        break
      sleep(5)
      self.league_client_controller.process()
      self.event_data_controller.process()
      self._process()

  async def _exec_ui_loop(self):
    """Execute the event loop responsible for Qt render and WebSocket events.
    """
    while True:
      self.application.processEvents()
      await asyncio.sleep(0, loop=self.ui_event_loop)
  
  def _start_thread(self, task):
    """Execute a thread with a given task.
    """
    thread = Thread(target=task)
    thread.start()
  
  async def exec_event_loop(self):
    """Execute the main orchestrating event loop.
    """
    self._start_thread(self._exec_client_loop_task)
    await self._exec_ui_loop()
  
  def set_app(self, app: QtWidgets.QApplication):
    self.application = app
