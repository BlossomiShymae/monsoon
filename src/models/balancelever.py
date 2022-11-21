from dataclasses import dataclass

@dataclass
class BalanceLever:
  """Data class for representing an ARAM balance lever.
  """
  # The name of a balance lever ("dmg_dealt, dmg_taken"...)
  name: str
  # The modifier a balance lever applies (0.8, 1.1...)
  modifier: float

  def _format_name(self) -> str:
    return self.name.replace("_", " ").title()
  
  def _format_modifier(self) -> str:
    percentage = int((self.modifier - 1.00) * 100)
    sign = "+" if percentage >= 0 else "-"
    return f"{sign} {percentage}"
  
  def format(self) -> str:
    """Return a formatted string of a balance lever. ("Dmg Dealt: -20%")

    Returns:
        str: Formatted string reperesentation of a balance lever.
    """
    return f"{self._format_name()}: {self._format_modifier()}"