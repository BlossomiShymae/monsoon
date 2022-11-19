import requests
from bs4 import BeautifulSoup
from models import BalanceModel

class LolFandom():
  def __init__(self):
    self.url = "https://leagueoflegends.fandom.com"
    self.__cache = self._fetch_aram_balance_changes()
    self.__balances_by_key = self._process_cache()

  def _fetch_aram_balance_changes(self):
    """Fetch and parse ARAM balance changes from the LoL Fandom ARAM article.

    Raises:
        Exception: Failed to get a valid request
        Exception: Failed to find any changes from table

    Returns:
        ResultSet[tag]: Set of 'tr' tags that are parsed from HTML table.
    """
    req = requests.get(f"{self.url}/wiki/ARAM")

    if req.status_code != 200:
      raise Exception("Failed to get ARAM balance changes from LoL Fandom")
    
    soup = BeautifulSoup(req.text, "html.parser")
    rows = soup.select("div.tabber table tbody tr")

    if len(rows) == 0:
      raise Exception("Failed to parse table from Lol Fandom; No rows found")

    return rows
  
  def _process_cache(self):
    """Process cache into a dictionary of balance changes using name as key.
    Below example indexed by raw response, NOT by the parsed response.
    tr[0] - Contains champion name
    tr[1] - Contains damage dealt
    tr[2] - Contains damage received
    tr[3] - Contains other changes
    """
    balance = {}
    for tr in self.__cache[1:]:
      champion_name = tr.contents[1].text.strip()
      balance.update({ champion_name: BalanceModel(
        champion_name=tr.contents[1].text.strip(),
        damage_dealt=tr.contents[3].text.strip(),
        damage_received=tr.contents[5].text.strip(),
        other_changes=tr.contents[7].text.strip()
      )})
    
    return balance

  
  def fetch_balance_by_champion_name(self, name) -> BalanceModel:
    """Finds a BalanceModel instance for a champion name. May return None as 
    not all champions have balance changes applied in ARAM.

    Args:
        name (str): Champion name to find with.

    Returns:
        BalanceModel: Represents the balance changes for a champion in ARAM.
    """
    return self.__balances_by_key.get(name)
