from enum import Enum
from PySide6 import QtWidgets

class QtStretches(Enum):
  HORIZONTAL = 0
  VERTICAL = 1

class QtHelpers():
  @staticmethod
  def create_size_policy(stretch: QtStretches, factor: int) -> QtWidgets.QSizePolicy:
    sp = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    if stretch is QtStretches.HORIZONTAL:
      sp.setHorizontalStretch(factor)
    elif stretch is QtStretches.VERTICAL:
      sp.setVerticalStretch(factor)
    return sp