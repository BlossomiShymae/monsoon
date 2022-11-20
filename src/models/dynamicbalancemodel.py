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