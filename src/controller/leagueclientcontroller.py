from win32.win32gui import EnumWindows, GetWindowRect, GetForegroundWindow, GetWindowText
from win32.win32process import GetWindowThreadProcessId
from constant import Monsoon

import subprocess
import re

class LeagueClientController():
  def __init__(self):
    self.process_name = "LeagueClientUx.exe"
    self.window = None

  def __on_enumerate_window__(self, window_handle, process_id):
    """Callback for EnumWindows to get League client window.

    Args:
        hwnd (object): Window handle.
        extra (object): Process id.

    Returns:
        bool: Condition to end EnumWindows
    """
    # Did we find the League client window associated with process id?
    if process_id in GetWindowThreadProcessId(window_handle):
      self.window = window_handle
      # Return False to end enumeration early for EnumWindows caller
      # http://timgolden.me.uk/pywin32-docs/win32gui__EnumWindows_meth.html
      return False
  
  def __parse_process_id__(self, data: str):
    """Parse process id from a data string using regular expression.

    Args:
        data (str): Raw data string output from process.

    Returns:
        int | None
    """
    match = re.search(r"\d+", data)
    if match == None:
      return None

    return int(match.group())
  

  def __find_window__(self, is_memoized=True):
    """Find the window associated with the League client process.

    Args:
        is_memoized (bool, optional): Use cached instance. Defaults to True.

    Returns:
        object | None: Window handle or None when no window is found.
    """
    data_string = str(subprocess.Popen(
      f"wmic PROCESS WHERE name='{self.process_name}' GET processid",
      shell=True,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE).communicate()[0]
    )
    process_id = self.__parse_process_id__(data_string)

    if is_memoized and self.window != None and process_id:
      return self.window

    self.window = None
    # Have to use try...except due to EnumWindows weird behavior when ending 
    # enumeration early. u.u
    try:
      EnumWindows(self.__on_enumerate_window__, process_id)
    except Exception:
      pass

    return self.window

  def is_active(self):
    """Test if the League client is active.

    Returns:
        bool: Existance of League client.
    """ 
    if (self.__find_window__(is_memoized=False)):
      return True
    return False
  
  def is_foreground(self):
    return self.window == GetForegroundWindow()

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