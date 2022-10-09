from api import DataDragon, LolFandom
from constant import WebSocketEvent
from model import SessionModel

import logging

class EventDataController():
  def __init__(self):
    self.dd_api = DataDragon()
    self.lf_api = LolFandom()
    self.events_queue = []
    self.is_active = False
    self.team_balances = []
    self.team_other_balances = []
    self.bench_balances = []

  def _clear_balances(self):
    """Clear balance queues.
    """
    self.team_balances.clear()
    self.team_other_balances.clear()
    self.bench_balances.clear()

  def __is_in_champ_select__(self, event_type: str) -> bool:
    return event_type == WebSocketEvent.CREATE or event_type == WebSocketEvent.UPDATE

  def __process__(self, event):
    """Process for any balance changes from event data.

    Args:
        event (object): Event object.
    """
    # Trait of an ARAM selection if the bench is enabled.
    if "benchEnabled" in event["data"] and event["data"]["benchEnabled"]:
      pass
    else:
      self._clear_balances()
      self.is_active = False
      return

    if "eventType" in event:
      event_type = event["eventType"]
      print(event_type)
      if self.__is_in_champ_select__(event_type):
        logging.debug("Showing the overlay! <3")
        self._clear_balances()
        
        # Get current session from League client
        bench_champions = event["data"]["benchChampions"]
        my_team = event["data"]["myTeam"]
        session = SessionModel(
          bench_champions=[champion["championId"] for champion in bench_champions],
          team_champions=[champion["championId"] for champion in my_team]
        )

        # Render balance changes into team rows
        if len(session.team_champions) > 1:
          for champion_id in session.team_champions:
            champion = self.dd_api.fetch_by_champion_id(champion_id)
            balance = self.lf_api.fetch_balance_by_champion_name(champion["name"])
            if balance == None:
              team_display = ""
              team_other_display = ""
            else:
              team_display = balance.format_minimal()
              team_other_display = balance.format()
            self.team_balances.append(team_display)
            self.team_other_balances.append(team_other_display)
        # Render balances changes into bench columns
        if len(session.bench_champions) > 1:
          for champion_id in session.bench_champions:
            champion = self.dd_api.fetch_by_champion_id(champion_id)
            balance = self.lf_api.fetch_balance_by_champion_name(champion["name"])
            if balance == None:
              bench_display = ""
            else:
              bench_display = balance.format()
            self.bench_balances.append(bench_display)
        self.is_active = True
      if event_type == WebSocketEvent.DELETE:
        logging.debug("Hiding the overlay. :c")
        self._clear_balances()
        self.is_active = False

  def get_state(self):
    """Get the state summary of the controller in a tuple format.

    Returns:
        tuple: (is_active, team_balances, team_other_balances, bench_balances)
    """
    return (self.is_active, self.team_balances, self.team_other_balances, self.bench_balances)

  def process(self):
    """Process all events in queue.
    """
    for event in self.events_queue:
      self.__process__(event)
    self.events_queue.clear()


