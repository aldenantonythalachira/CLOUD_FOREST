import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_my_assets():
  user = anvil.users.get_user()
  if user == None:
    return []
  
  if not user["purchased_assets"]:
    return []
  
  assets = []
  for asset in user["purchased_assets"]:
    asset_info = app_tables.assets.get(id=asset)
    assets.append(asset_info)
  
  return assets

