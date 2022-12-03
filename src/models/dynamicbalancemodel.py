from models import BalanceLever
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class DynamicBalanceModel:
  """Data class that represents balance levers for a champion. The amount of
  levers can differ for each champion.
  """
  champion_name: str
  balance_levers: List[BalanceLever]
  champion_icon: Optional[bytes] = None

  def _format_champion_name(self) -> str:
    return f"{self.champion_name}"
  
  def format(self):
    """Return a formatted label string of dynamic balance changes for champion.

    Returns:
        str: Formatted string representation of dynamic balance changes.
    """
    label = self._format_champion_name()
    for i, balance_lever in enumerate(self.balance_levers):
      spacer = "\n" if i % 2 == 0 else " "
      label += f"{spacer}{balance_lever.format()}"
    return label

  def format_balance_levers(self):
    """Return an alphabetically sorted list of balance lever strings.

    Returns:
        List[str]
    """ 
    balance_lever_strings = [x.format() for x in self.balance_levers]
    balance_lever_strings.sort()
    return balance_lever_strings