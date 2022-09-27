from PySide6 import QtWidgets, QtCore
from api import DataDragon, LolFandom
from constant import Monsoon, Stylesheet
from controller import LeagueClientController
from model import SessionModel

class MainView(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    # Set instance variables
    self.client_controller = LeagueClientController()
    self.dd_api = DataDragon()
    self.lf_api = LolFandom()
    self.event_data_list = []
    (self.hbox, self.hbox_layout) = self.__create_hbox()
    (self.left_vbox, self.left_vbox_layout) = self.__create_vbox()
    (self.middle_vbox, self.middle_vbox_layout) = self.__create_vbox()
    (self.right_vbox, self.right_vbox_layout) = self.__create_vbox()
    (self.team_vbox, self.team_vbox_layout) = self.__create_vbox()
    self.team_rows = [QtWidgets.QLabel("") for i in range(5)]

    # Set horizontal box columns
    self.hbox_layout.addWidget(self.left_vbox, 35)
    self.hbox_layout.addWidget(self.middle_vbox, 58)
    self.hbox_layout.addWidget(self.right_vbox, 35)

    # Set left box column (Team Champions)
    self.left_vbox_layout.addWidget(QtWidgets.QLabel(""), 2)
    self.left_vbox_layout.addWidget(self.team_vbox, 8)
    self.left_vbox_layout.addWidget(QtWidgets.QLabel(""), 3)

    # Set team rows to left box column
    for row in self.team_rows:
      self.team_vbox_layout.addWidget(row)

    # Set window properties
    self.resize(Monsoon.WIDTH.value, Monsoon.HEIGHT.value)
    self.setWindowTitle(Monsoon.TITLE.value)
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    self.setCentralWidget(self.hbox)

  def __create_hbox(self):
    hbox = QtWidgets.QGroupBox()
    hbox_layout = QtWidgets.QHBoxLayout()
    hbox.setLayout(hbox_layout)
    hbox.setStyleSheet(Stylesheet.value())

    return (hbox, hbox_layout)
  
  def __create_vbox(self):
    vbox = QtWidgets.QGroupBox()
    vbox_layout = QtWidgets.QVBoxLayout()
    vbox.setLayout(vbox_layout)
    vbox.setStyleSheet(Stylesheet.value())

    return (vbox, vbox_layout)
    
  @QtCore.Slot()
  def refresh(self):
    if (self.client_controller.is_active()):
      (left, top, right, bottom) = self.client_controller.find()

      # Calculate window dimensions
      height = bottom - top
      width = right - left

      # Process the event data list passed from callback
      for data in self.event_data_list:
        # Trait of an ARAM selection if the bench is enabled.
        # if "benchEnabled" in data and data["benchEnabled"]:
          if "eventType" in data:
            if data["eventType"] == "Update" or data["eventType"] == "Create":
              print("SHOWING")
              
              # Get current session from League client
              bench_champions = data["data"]["benchChampions"]
              my_team = data["data"]["myTeam"]
              session = SessionModel(
                bench_champions=[champion["championId"] for champion in bench_champions],
                team_champions=[champion["championId"] for champion in my_team]
              )

              # Render balance changes into team rows
              for i, champion_id in enumerate(session.team_champions):
                champion = self.dd_api.fetch_by_champion_id(champion_id)
                balance = self.lf_api.fetch_balance_by_champion_name(champion["name"])
                if balance == None:
                  display = ""
                else:
                  display = f"Damage dealt: {balance.damage_dealt}\nDamage received: {balance.damage_received}"
                self.team_rows[i].setText(display)
              self.show()
            if data["eventType"] == "Delete":
              print("HIDING")
              # Clear team rows
              for row in self.team_rows:
                row.setText("")
              self.hide()
      self.event_data_list.clear()

      # Adjust view based on League client (lock onto it)
      self.setGeometry(left, top, width, height)
    pass

