from ._anvil_designer import MyAssetsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..AssetDetailsItem import AssetDetailsItem

class MyAssets(MyAssetsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_assets()
    
  def render_asset(self, asset_id):
    self.content_panel.clear()
    
  def load_assets(self,**event_args):
    assets = anvil.server.call("get_my_assets")
    
    if len(assets) > 0:
      self.no_assets_label.visible = False
    
    asset_panel = GridPanel()
    
    for i, asset in enumerate(assets):
      c = AssetDetailsItem(farmer_name=asset["farmer_name"], location=asset["location"],cptpm=asset["cptpm"], trees_available=asset["trees_available"],rental_duration=asset["rental_duration"],total=asset["total"])
      asset_panel.add_component(c, row=str(i//2), width_xs=6)
    
    self.content_panel.add_component(asset_panel)

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pass

  def load_asset(self,**event_args):
    """This method is called when the column panel is shown on the screen"""
    pass



