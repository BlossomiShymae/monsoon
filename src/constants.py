from enum import Enum

class Monsoon():
  TITLE = "Monsoon"
  VERSION = "2.0.0-alpha"
  AUTHOR = "MissUwuieTime"
  LEGAL = "Monsoon isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc."
  WIDTH = 1280
  HEIGHT = 720


class Workers(Enum):
  LOCKFILE_WATCHER = 0
  LCU_EVENT_PROCESSOR = 1
