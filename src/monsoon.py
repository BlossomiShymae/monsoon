from container import Container
from services import ApplicationHostService
import services
import views

import asyncio
from dependency_injector.wiring import Provide, inject
import logging

@inject
def main(
  application_host_service: ApplicationHostService = Provide[Container.application_host_service]):
  loop = asyncio.get_event_loop()
  try:
    loop.run_until_complete(application_host_service.start_async())
  except KeyboardInterrupt:
    loop.run_until_complete(application_host_service.stop_async())

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  container = Container()
  container.init_resources()
  container.wire(modules=[__name__], packages=[services, views])

  main()