from win32.win32gui import FindWindow, GetWindowRect, GetForegroundWindow, GetWindowText
from constant import Monsoon

class LeagueClientController():
  def __init__(self):
    self.window_name = "League of Legends"

  def __find_window__(self):
    return FindWindow(None, self.window_name)

  def is_active(self):
    """Test if the League client is active.

    Returns:
        bool: Existance of League client.
    """ 
    if (self.__find_window__()):
      return True
    return False
  
  def is_foreground(self):
    return self.window_name == GetWindowText(GetForegroundWindow())

  def is_overlayed(self):
    return Monsoon.TITLE.value == GetWindowText(GetForegroundWindow())

  def find(self):
    """Gets the window coordinates of the League client.

    Returns:
        tuple: (left, top, right, bottom)
    """
    window_handle = self.__find_window__()
    window_rect = GetWindowRect(window_handle)
    
    return window_rect