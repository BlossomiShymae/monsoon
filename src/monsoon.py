from PySide6 import QtWidgets, QtCore, QtGui
from constant import Embedded, Stylesheet
from controller import EventDataController
from service import TimerService
from template import SystemTray
from view import MainView
import logging
import willump
import asyncio
import json

def milliseconds_from_fps(fps: int) -> int:
  """Calculate milliseconds from the rate of frames per second.

  Args:
      fps (int): Frames per second

  Returns:
      int: Milliseconds
  """
  return (1 / fps) * 1000

def use_embedded_icon(app: QtWidgets.QApplication, b64_image):
  """Use a Base64 encoded image as the application icon.

  Args:
      app (QtWidgets.QApplication): Qt Application
      b64_image (str): Base64 encoded image string
  """
  pixmap = QtGui.QPixmap()
  pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))
  icon = QtGui.QIcon(pixmap)
  app.setWindowIcon(icon)

async def data_callback(data, controller: EventDataController):
  """Pass WebSocket event data to the event data controller.

  Args:
      data (object): League client event data
      controller (EventDataController): Controller for WebSocket event data
  """
  print(json.dumps(data, indent=4, sort_keys=True))
  controller.events_queue.append(data)

async def main():
  """Asynchronously run the main application.
  """
  logging.basicConfig(level=logging.DEBUG)

  global wllp
  wllp = await willump.start()

  app = QtWidgets.QApplication([])
  app.setStyleSheet(Stylesheet.value())
  event_data_controller = EventDataController()
  view = MainView(event_data_controller=event_data_controller)
  subscription = await wllp.subscribe(
    "OnJsonApiEvent_lol-champ-select_v1_session",
     default_handler=lambda data: data_callback(data, event_data_controller)
  )

  # Setup system tray icon
  tray = SystemTray()
  tray.show()

  use_embedded_icon(app, Embedded.icon())

  # Refresh view based on update tick rate (20fps)
  update_timer = TimerService(milliseconds_from_fps(20))
  update_timer.add_slot(view.refresh)

  async def exec_loop():
    """ Execute the event loop that processes both Qt and asyncip loops.
    """
    while True:
      app.processEvents()
      await asyncio.sleep(0)

  await exec_loop()


if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  try:
    loop.run_until_complete(main())
  except KeyboardInterrupt:
    loop.run_until_complete(wllp.close())
    print()