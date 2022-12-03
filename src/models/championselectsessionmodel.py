from dataclasses import dataclass
from typing import List

from lcu_driver.events.responses import WebsocketEventResponse


@dataclass
class ChampionSelectSessionModel:
    """Class for keeping track of an active champion select session in League.
    """
    available_champion_ids: List[int]
    team_champion_ids: List[int]
    is_bench_enabled: bool
    websocket_event_type: str

    @classmethod
    def from_websocket_event_response(cls, event: WebsocketEventResponse):
        bench_champions = event.data["benchChampions"]
        available_champion_ids = None
        if bench_champions:
            available_champion_ids = [int(x["championId"]) for x in bench_champions]
        teammates = event.data["myTeam"]
        team_champion_ids = [int(x["championId"]) for x in teammates]
        is_bench_enabled = bool(event.data["benchEnabled"])
        websocket_event_type = str(event.type)
        return cls(
            available_champion_ids=available_champion_ids,
            team_champion_ids=team_champion_ids,
            is_bench_enabled=is_bench_enabled,
            websocket_event_type=websocket_event_type
        )
