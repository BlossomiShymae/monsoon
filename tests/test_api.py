import pytest
from src.apis import DataDragon, LolFandom


class TestApis:
    class TestDataDragon:
        def test_api_returns_champion_data(self):
            champion_id = 37
            api = DataDragon()
            data = api.fetch_by_champion_id(champion_id)
            assert data['id'] == 'Sona'

    class TestLolFandom:
        def test_api_has_processed_dynamic_data(self):
            champion_name = 'Sona'
            api = LolFandom()
            assert api.fetch_dynamic_balance_by_champion_name(champion_name) is not None
