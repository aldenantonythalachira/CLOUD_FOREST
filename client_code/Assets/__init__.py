from ._anvil_designer import AssetsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..AssetItem import AssetItem
from ..Checkout import Checkout

class Assets(AssetsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_assets()
    
  def back(self):
    self.content_panel.clear()
    self.load_assets()
    
  def render_checkout(self, asset_id):
    self.content_panel.clear()
    self.content_panel.add_component(Checkout(asset_id, self.back))

  def load_assets(self):
    assets = anvil.server.call("get_all_assets").search()
    asset_panel = GridPanel()
    
    for i, asset in enumerate(assets):
       c = AssetItem(asset_id=asset["id"],farmer_name=asset["farmer_name"], location=asset["location"], image=asset["image"],cptpm=asset["cptpm"], trees_available=asset["trees_available"],rental_duration=asset["rental_duration"],total=asset["total"], button_callback=self.render_checkout)
       asset_panel.add_component(c, row=str(i//2), width_xs=6)
    
    self.content_panel.add_component(asset_panel)
  