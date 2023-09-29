import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def charge_user(token, email, asset_name):
  stripe_customer = anvil.stripe.new_customer(email, token)
  price = app_tables.assets.get(id_name=asset_name)['price']
  user = anvil.users.get_user()
  if user["purchased_assets"] == None:
    user["purchased_assets"] = []
  
  if asset_name in user["purchased_assets"]:
    return
  
  result = stripe_customer.charge(amount=price*100, currency="USD")
  user["purchased_assets"] = user["purchased_assets"] + [asset_name]

