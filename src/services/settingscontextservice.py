from PySide6 import QtCore

class SettingsSchema():
  DEFAULT = ("", "")

class SettingsContextService():
  def __init__(self) -> None:
    self.settings = QtCore.QSettings("MissUwuieTime", "Monsoon")
  
  def get(self, schema_tuple: tuple):
    (key, default) = schema_tuple
    return self.settings.value(key, default)
  
  def set(self, key: str, value):
    self.settings.setValue(key, value)
    self.settings.sync()