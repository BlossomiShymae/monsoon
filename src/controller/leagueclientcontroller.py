from win32.win32gui import FindWindow, GetWindowRect

class LeagueClientController():
  def __init__(self):
    pass

  def __find_window(self):
    return FindWindow(None, "League of Legends")

  def is_active(self):
    """Test if the League client is active.

    Returns:
        bool: Existance of League client.
    """ 
    if (self.__find_window()):
      return True
    return False

  def find(self):
    """Gets the window coordinates of the League client.

    Returns:
        tuple: (left, top, right, bottom)
    """
    window_handle = self.__find_window()
    window_rect = GetWindowRect(window_handle)
    
    return window_rect