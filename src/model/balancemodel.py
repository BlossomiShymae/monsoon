from dataclasses import dataclass

@dataclass
class BalanceModel:
  """Class for caching ARAM balance changes of a champion from LoL Fandom.
  """
  champion_name: str
  damage_dealt: int
  damage_received: int
  other_changes: str
