from models import BalanceLever
from typing import List
from dataclasses import dataclass

@dataclass
class DynamicBalanceModel:
  """Data class that represents balance levers for a champion. The amount of
  levers can differ for each champion.
  """
  champion_name: str
  balance_levers: List[BalanceLever]

  def _format_champion_name(self) -> str:
    return f"{self.champion_name}"
  
  def format(self):
    """Return a formatted label string of dynamic balance changes for champion.

    Returns:
        str: Formatted string representation of dynamic balance changes.
    """
    label = self._format_champion_name()
    for balance_lever in self.balance_levers:
      label += f"\n{balance_lever.format()}"
