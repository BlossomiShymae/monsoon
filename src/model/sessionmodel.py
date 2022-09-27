from dataclasses import dataclass
from typing import List

@dataclass
class SessionModel:
  """Class for keeping track of a champion select session in League client.
  """
  bench_champions: List[int]
  team_champions: List[int]