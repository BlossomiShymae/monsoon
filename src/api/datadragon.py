import requests

class DataDragon():
  def __init__(self):
    self.url = "https://ddragon.leagueoflegends.com"
    self.latest_version = self.__fetch_latest_version__()
    self.champions = self.__fetch_champions__()
  
  def __fetch_latest_version__(self):
    req = requests.get(f"{self.url}/api/versions.json")

    if req.status_code != 200:
      raise Exception("Failed to get latest version from DataDragon")
    
    if len(req.json()) == 0:
      raise Exception("Received empty versions list from DataDragon")

    return req.json()[0]

  def __fetch_champions__(self):
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