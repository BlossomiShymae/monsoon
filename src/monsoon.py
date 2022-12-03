from container import Container
from services import ApplicationHostService
import services
import views
import viewmodels

from dependency_injector.wiring import Provide, inject
import logging


@inject
def main(
  application_host_service: ApplicationHostService = Provide[Container.application_host_service]):
  try:
    application_host_service.start()
  except KeyboardInterrupt:
    application_host_service.stop()

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  container = Container()
  container.init_resources()
  container.wire(modules=[__name__], packages=[services, views, viewmodels])

  main()