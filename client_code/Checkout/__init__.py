from ._anvil_designer import CheckoutTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe

class Checkout(CheckoutTemplate):
  def __init__(self, id, back_button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.back_button_callback = back_button_callback
    self.update_form(id)
  
  def update_form(self, id):
    asset = anvil.server.call('get_asset_details', id)
    self.asset = asset
    self.name_label.text = asset["farmer_name"]
    self.description_label.text = asset['description']
    self.price_label.text = f"${asset['total']} USD"
    self.image_content.source = asset['image']

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    if anvil.users.get_user() == None:
      anvil.users.login_with_form()
    
    user = anvil.users.get_user()
    if user == None:
      alert("Please sign in!")
      return
    
    if user["purchased_assets"] and self.asset["id"] in user["purchased_assets"]:
      alert("You already own this asset")
      return
  
    token, info = stripe.checkout.get_token(amount=self.asset["total"]*100, currency="SGD", title=self.asset["farmer_name"])
    try:
      anvil.server.call("charge_user", token, user["email"], self.asset["id_name"])
      alert("Success")
    except Exception as e:
      alert(str(e))
    
  
  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()


