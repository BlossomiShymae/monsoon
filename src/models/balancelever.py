from dataclasses import dataclass

@dataclass
class BalanceLever:
  """Data class for representing an ARAM balance lever.
  """
  # The name of a balance lever ("dmg_dealt, dmg_taken"...)
  name: str
  # The modifier a balance lever applies (0.8, 1.1...)
  modifier: float