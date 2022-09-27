from PySide6 import QtWidgets, QtCore, QtGui
from constant import Embedded
from service import TimerService
from view import MainView
import logging
import willump
import asyncio
import json

def milliseconds_from_fps(fps: int) -> int:
  return (1 / fps) * 1000

def use_embedded_icon(app: QtWidgets.QApplication, b64_image):
  pixmap = QtGui.QPixmap()
  pixmap.loadFromData(QtCore.QByteArray.fromBase64(b64_image))
  icon = QtGui.QIcon(pixmap)
  app.setWindowIcon(icon)

async def data_callback(data):
  pass


async def main():
  logging.basicConfig(level=logging.DEBUG)

  global wllp
  wllp = await willump.start()
  subscription = await wllp.subscribe("OnJsonApiEvent_lol-champ-select_v1_session", default_handler=print_data_callback)

  app = QtWidgets.QApplication([])

  view = MainView()
  view.show()

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