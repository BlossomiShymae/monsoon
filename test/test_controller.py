import pytest
from controllers import LeagueClientController

# Make sure to run this test file with the League client running.
# Otherwise, please skip. :3

class TestControllers():
  class TestLeagueClientController():
    def test_is_active_returns_true(self):
      controller = LeagueClientController()
      assert controller.is_active() == True
    
    def test_find_returns_any(self):
      controller = LeagueClientController()
      assert controller.find() != None
