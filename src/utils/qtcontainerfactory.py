from enum import Enum
from PySide6 import QtWidgets

class QtWidgetContainer():
  def __init__(
    self, 
    container_widget: QtWidgets.QWidget, 
    layout: QtWidgets.QLayout
  ) -> None:
    self.container_widget = container_widget
    self.layout = layout

class QtContainerLayouts(Enum):
  GRID = 0
  VERTICAL = 1
  HORIZONTAL = 2
  
class QtContainerFactory():
  @staticmethod
  def create(
    layout_type: QtContainerLayouts, 
    container: QtWidgets.QWidget = QtWidgets.QFrame()
  ) -> QtWidgetContainer:
    layout = None
    if layout_type is QtContainerLayouts.GRID:
      layout = QtWidgets.QGridLayout()
    elif layout_type is QtContainerLayouts.HORIZONTAL:
      layout = QtWidgets.QHBoxLayout()
    elif layout_type is QtContainerLayouts.VERTICAL:
      layout = QtWidgets.QVBoxLayout()
    else:
      raise Exception("Invalid container layout enum")
    
    layout.setSpacing(0)
    layout.setContentsMargins(0,0,0,0)
    container.setLayout(layout)
    return QtWidgetContainer(container, layout)