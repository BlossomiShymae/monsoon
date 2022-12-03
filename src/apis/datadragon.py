import requests


class DataDragon():
  def __init__(self):
    self.url = "https://ddragon.leagueoflegends.com"
    self.latest_version = self._fetch_latest_version()
    self.champions = self._fetch_champions()
    self.champion_icons = dict()
  
  def _fetch_latest_version(self):
    req = requests.get(f"{self.url}/api/versions.json")

    if req.status_code != 200:
      raise Exception("Failed to get latest version from DataDragon")
    
    if len(req.json()) == 0:
      raise Exception("Received empty versions list from DataDragon")

    return req.json()[0]

  def _fetch_champions(self):
    req = requests.get(f"{self.url}/cdn/{self.latest_version}/data/en_US/champion.json")

    if req.status_code != 200:
      raise Exception("Failed to get champions from DataDragon")
    
    return req.json()
  
  def fetch_by_champion_id(self, champion_id):
    data = self.champions["data"]
    for id in data:
      if (int(data[id]["key"]) == champion_id):
        return data[id]
    
    return None
  
  def fetch_icon_by_champion_id(self, champion_id):
    data = self.champions["data"]
    champion_name = None
    for id in data.keys():
      if (int(data[id]["key"]) == champion_id):
        champion_name = id
        break
    
    if champion_name is None:
      raise Exception("Invalid champion id")

    if not champion_name in self.champion_icons:
      req = requests.get(f"{self.url}/cdn/{self.latest_version}/img/champion/{champion_name}.png", stream=True)
      if req.status_code != 200:
        raise Exception("Failed to get champion icon from DataDragon")
      self.champion_icons[champion_name] = req.content

    return self.champion_icons[champion_name]