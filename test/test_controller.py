import pytest
from controller import LeagueClientController

# Make sure to run this test file with the League client running.
# Otherwise, please skip. :3

class TestController():
  class TestLeagueClientController():
    def test_is_active_returns_true():
      controller = LeagueClientController()
      assert controller.is_active() == True
