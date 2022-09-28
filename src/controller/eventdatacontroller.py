from api import DataDragon, LolFandom
from model import SessionModel

class EventDataController():
  def __init__(self):
    self.dd_api = DataDragon()
    self.lf_api = LolFandom()
    self.events_queue = []
    self.is_active = False
    self.team_balances = []

  def __process(self, event):
    """Process for any balance changes from event data.

    Args:
        event_data (_type_): _description_
    """
    # Trait of an ARAM selection if the bench is enabled.
    # if "benchEnabled" in data and data["benchEnabled"]:
    if "eventType" in event:
      if event["eventType"] == "Update" or event["eventType"] == "Create":
        print("SHOWING")
        
        # Get current session from League client
        bench_champions = event["data"]["benchChampions"]
        my_team = event["data"]["myTeam"]
        session = SessionModel(
          bench_champions=[champion["championId"] for champion in bench_champions],
          team_champions=[champion["championId"] for champion in my_team]
        )

        # Render balance changes into team rows
        self.team_balances.clear()
        for champion_id in session.team_champions:
          champion = self.dd_api.fetch_by_champion_id(champion_id)
          balance = self.lf_api.fetch_balance_by_champion_name(champion["name"])
          if balance == None:
            display = ""
          else:
            display = balance.format()
          self.team_balances.append(display)
        self.is_active = True
      if event["eventType"] == "Delete":
        print("HIDING")
        self.team_balances.clear()
        self.is_active = False

  def get_state(self):
    """Get the state summary of the controller in a tuple format.

    Returns:
        tuple: (is_active, team_balances)
    """
    return (self.is_active, self.team_balances)

  def process(self):
    """Process all events in queue
    """
    for event in self.events_queue:
      self.__process(event)
    self.events_queue.clear()


