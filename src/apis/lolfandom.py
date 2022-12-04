import lupa
import requests
from bs4 import BeautifulSoup
from lupa import LuaRuntime

from models import DynamicBalanceModel, BalanceLever


class LolFandom:
    def __init__(self):
        self.url = "https://leagueoflegends.fandom.com"
        # Upstream; parses from Lua data module
        self.__championdata_module = self._fetch_championdata_module()
        self.__dynamic_balances_by_key = self._process_championdata_module()

    def fetch_dynamic_balance_by_champion_name(self, name) -> DynamicBalanceModel:
        """Finds a DynamicBalanceModel instance for a champion name. May return None
    as not all champions have balance changes applied in ARAM.

    Args:
        name (str): Champion name to find with.

    Returns:
        DynamicBalanceModel: Represents the dynamic balance changes for a 
        champion in ARAM from Module:ChampionData.
    """
        value = self.__dynamic_balances_by_key.get(name)
        if not value:
            value = DynamicBalanceModel(name, [])
        return value

    def _fetch_championdata_module(self) -> str:
        """Fetch Module:ChampionData from LoL Fandom that contains ARAM balance
    changes. Returns extracted Lua code.

    Raises:
        Exception: Response not 200
        Exception: Failed to select module

    Returns:
        str: Raw Lua code which itself returns table of champion statistics.
    """
        req = requests.get(f"{self.url}/wiki/Module:ChampionData/data")

        if req.status_code != 200:
            raise Exception("Failed to get Module:ChampionData from LoL Fandom")

        soup = BeautifulSoup(req.text, "html.parser")
        select = soup.select("pre.mw-code")
        if len(select) != 1:
            raise Exception("Failed to select Module:ChampionData from LoL Fandom")

        championdata_module = select[0].text
        return championdata_module

    def _process_championdata_module(self):
        """Process ChampionData modue by parsing Lua data table into dict of dynamic
    balances.
    """

        # Setup attribute handler to protect Python space from Lua
        def filter_attribute_access(obj, attr_name, is_setting):
            raise AttributeError("access denied")

        # Setup Lua runtime
        lua = LuaRuntime(
            unpack_returned_tuples=True,
            attribute_filter=filter_attribute_access,
            register_eval=False)
        # Block access to dangerous functions in Lua space
        for key in list(lua.globals()):
            if key != "_G":
                del lua.globals()[key]
                # Sanitize and format Lua code
        code = self.__championdata_module.strip()
        code = code.replace("return", "")
        code = code.replace("function", "")
        code = code.replace("(", "")
        code = code.replace(")", "")
        code = code.replace("-- <pre>", "")
        code = code.replace("-- </pre>", "")
        code = code.replace("-- [[Category:Lua]]", "")
        # Run Lua table
        table = lua.eval(code)
        # Ensure a Lua table is actually returned as a security precaution
        if lupa.lua_type(table) != "table":
            raise Exception("Failed to evaluate Module:ChampionData, stopping as security precaution")

        # Transform into list of (key, value) tuples
        items = list(table.items())
        dynamic_balances = {}
        # Create dynamic balance model data for each champion
        for kv_tuple in items:
            champion_name = kv_tuple[0]
            aram_stats = kv_tuple[1]["stats"]["aram"]
            # None type means there is no ARAM changes for champion
            if aram_stats is not None:
                balance_items = list(aram_stats.items())
                balance_levers = []
                for balance_tuple in balance_items:
                    balance_levers.append(BalanceLever(balance_tuple[0], balance_tuple[1]))
                # Insert new model into dictionary
                dynamic_balances.update({champion_name: DynamicBalanceModel(
                    champion_name=champion_name,
                    balance_levers=balance_levers
                )})

        return dynamic_balances
