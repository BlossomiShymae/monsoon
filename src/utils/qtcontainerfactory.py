from enum import Enum
from PySide6 import QtWidgets

class QtWidgetContainer():
  def __init__(
    self, 
    container: QtWidgets.QWidget, 
    layout: QtWidgets.QLayout
  ) -> None:
    self.container = container
    self.layout = layout

class QtContainerLayouts(Enum):
  GRID = 0
  VERTICAL = 1
  HORIZONTAL = 2
  STACKED = 3
  
class QtContainerFactory():
  @staticmethod
  def create(
    layout_type: QtContainerLayouts, 
    container: QtWidgets.QWidget = None
  ) -> QtWidgetContainer:
    if container is None:
      container = QtWidgets.QFrame()
    layout = None
    if layout_type is QtContainerLayouts.GRID:
      layout = QtWidgets.QGridLayout()
    elif layout_type is QtContainerLayouts.HORIZONTAL:
      layout = QtWidgets.QHBoxLayout()
    elif layout_type is QtContainerLayouts.VERTICAL:
      layout = QtWidgets.QVBoxLayout()
    elif layout_type is QtContainerLayouts.STACKED:
      layout = QtWidgets.QStackedLayout()
    else:
      raise Exception("Invalid container layout enum")
    
    layout.setSpacing(0)
    layout.setContentsMargins(0,0,0,0)
    container.setLayout(layout)
    return QtWidgetContainer(container, layout)