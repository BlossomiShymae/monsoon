import os
import sys
sys.path.append(os.path.abspath("./src/"))

from apis import LolFandom, DataDragon
from models import DynamicBalanceModel
from services import WorkerService, ApiService
from views import AppWindowView
from viewmodels import AppWindowViewModel
from PySide6 import QtWidgets
import qdarktheme

app = QtWidgets.QApplication()
app.setStyleSheet(qdarktheme.load_stylesheet())
worker_service = WorkerService()
api_service = ApiService()
viewmodel = AppWindowViewModel(worker_service=worker_service, api_service=api_service)
view = AppWindowView(app_window_viewmodel=viewmodel)
lf_api = LolFandom()
dd_api = DataDragon()

# Setup data
sona_balance = lf_api.fetch_dynamic_balance_by_champion_name("Sona")
sona_balance.champion_icon = dd_api.fetch_icon_by_champion_id(37)
seraphine_balance = lf_api.fetch_dynamic_balance_by_champion_name("Seraphine")
seraphine_balance.champion_icon = dd_api.fetch_icon_by_champion_id(147)
janna_balance = lf_api.fetch_dynamic_balance_by_champion_name("Janna")
janna_balance.champion_icon = dd_api.fetch_icon_by_champion_id(40)
soraka_balance = lf_api.fetch_dynamic_balance_by_champion_name("Soraka")
soraka_balance.champion_icon = dd_api.fetch_icon_by_champion_id(16)
nami_balance = lf_api.fetch_dynamic_balance_by_champion_name("Nami")
nami_balance.champion_icon = dd_api.fetch_icon_by_champion_id(267)

akali_balance = lf_api.fetch_dynamic_balance_by_champion_name("Akali")
akali_balance.champion_icon = dd_api.fetch_icon_by_champion_id(84)
qiyana_balance = lf_api.fetch_dynamic_balance_by_champion_name("Qiyana")
qiyana_balance.champion_icon = dd_api.fetch_icon_by_champion_id(246)
neeko_balance = lf_api.fetch_dynamic_balance_by_champion_name("Neeko")
neeko_balance.champion_icon = dd_api.fetch_icon_by_champion_id(76)
lillia_balance = lf_api.fetch_dynamic_balance_by_champion_name("Lillia")
lillia_balance.champion_icon = dd_api.fetch_icon_by_champion_id(876)
lux_balance = lf_api.fetch_dynamic_balance_by_champion_name("Lux")
lux_balance.champion_icon = dd_api.fetch_icon_by_champion_id(99)
ashe_balance = lf_api.fetch_dynamic_balance_by_champion_name("Ashe")
ashe_balance.champion_icon = dd_api.fetch_icon_by_champion_id(22)
gwen_balance = lf_api.fetch_dynamic_balance_by_champion_name("Gwen")
gwen_balance.champion_icon = dd_api.fetch_icon_by_champion_id(887)
zyra_balance = lf_api.fetch_dynamic_balance_by_champion_name("Zyra")
zyra_balance.champion_icon = dd_api.fetch_icon_by_champion_id(143)
xayah_balance = lf_api.fetch_dynamic_balance_by_champion_name("Xayah")
xayah_balance.champion_icon = dd_api.fetch_icon_by_champion_id(498)
ahri_balance = lf_api.fetch_dynamic_balance_by_champion_name("Ahri")
ahri_balance.champion_icon = dd_api.fetch_icon_by_champion_id(103)

# Simulate app by passing data to the viewmodel
viewmodel.available_champion_dynamic_balances = [
  akali_balance,
  qiyana_balance,
  neeko_balance,
  lillia_balance,
  lux_balance,
  ashe_balance,
  gwen_balance,
  zyra_balance,
  xayah_balance,
  ahri_balance
]
viewmodel.team_champion_dynamic_balances = [
  sona_balance,
  seraphine_balance,
  janna_balance,
  soraka_balance,
  nami_balance,
]

view.show()
try:
  app.exec()
except KeyboardInterrupt:
  sys.exit(0)