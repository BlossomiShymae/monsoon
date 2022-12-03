from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from src.apis import DataDragon, LolFandom


class ApiService:
    def __init__(
            self
    ):
        self.data_dragon = DataDragon()
        self.lol_fandom = LolFandom()
