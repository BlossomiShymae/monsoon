from win32.win32gui import EnumWindows, GetWindowRect, GetForegroundWindow, GetWindowText
from win32.win32process import GetWindowThreadProcessId
from constants import Monsoon

import subprocess
import re

class LeagueClientController():
  def __init__(self):
    self.process_name = "LeagueClientUx.exe"
    self.window = None

  def _on_enumerate_window(self, window_handle, process_id):
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
  
  def _parse_process_id(self, data: str):
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
  

  def _find_window(self, is_memoized=True):
    """Find the window associated with the League client process. Mutative.

    Args:
        is_memoized (bool, optional): Use cached instance. Defaults to True.

    Returns:
        object | None: Window handle or None when no window is found.
    """
    if is_memoized and self.window != None:
      return self.window

    data_string = str(subprocess.Popen(
      f"wmic PROCESS WHERE name='{self.process_name}' GET processid",
      shell=True,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE).communicate()[0]
    )
    process_id = self._parse_process_id(data_string)

    # Have to use try...except due to EnumWindows weird behavior when ending 
    # enumeration early. u.u
    is_window_found = False
    try:
      EnumWindows(self._on_enumerate_window, process_id)
    except Exception:
      is_window_found = True
    if not is_window_found:
      self.window = None

    return self.window
  
  def process(self):
    """Process the controller to find the window for the League client.
    """
    self._find_window(is_memoized=False)

  def is_active(self):
    """Test if the League client is active.

    Returns:
        bool: Existance of League client.
    """ 
    # Window does not exist yet
    if not self.window:
      return False
    # Window was used but has been exited
    if not self.find():
      return False
    if (self._find_window()):
      return True

    return False
  
  def is_foreground(self):
    return self.window == GetForegroundWindow()

  def is_overlayed(self):
    return Monsoon.TITLE.value == GetWindowText(GetForegroundWindow())

  def find(self):
    """Gets the window coordinates of the League client.

    Returns:
        tuple | None: (left, top, right, bottom) or None when window does not
        exist.
    """
    window_handle = self._find_window()
    try:
      window_rect = GetWindowRect(window_handle)
    except Exception:
      return None
    
    return window_rect