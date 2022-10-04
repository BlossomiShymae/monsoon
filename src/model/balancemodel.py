from dataclasses import dataclass

@dataclass
class BalanceModel:
  """Data class for caching ARAM balance changes of a champion from LoL Fandom.
  """
  champion_name: str
  damage_dealt: str
  damage_received: str
  other_changes: str

  def __format_champion_name__(self):
    return f"{self.champion_name}"

  def __format_damage_dealt__(self):
    return f"Damage dealt: {self.damage_dealt}"
  
  def __format_damage_received__(self):
    return f"Damage received: {self.damage_received}"
  
  def __format_other_changes__(self):
    return f"Other changes: {self.other_changes}"

  def format(self):
    """Return a formatted label string of balance changes for a champion.

    Returns:
        str: Formatted string representation of balance changes.
    """
    label = self.__format_champion_name__()
    if len(self.damage_dealt) > 0:
      label += f"\n{self.__format_damage_dealt__()}" 
    if len(self.damage_received) > 0:
      label += f"\n{self.__format_damage_received__()}"
    if len(self.other_changes) > 0:
      label += f"\n{self.__format_other_changes__()}"
    
    return label
  
  def format_minimal(self):
    """Return a minimal formatted label string of balance changes for a champion.

    Returns:
        str: Minimal formatted string representation of balance changes.
    """
    label = ""
    if len(self.damage_dealt) > 0:
      label += f"{self.__format_damage_dealt__()}\n"
    if len(self.damage_received) > 0:
      label += f"{self.__format_damage_received__()}\n"
    
    return label
