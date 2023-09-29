from ._anvil_designer import AssetItemTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AssetItem(AssetItemTemplate):
  def __init__(self, farmer_name, location, image, cptpm, trees_available, period_chosen,total,button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.farmer_name.content = farmer_name
    self.location.content = location
    self.image_tree.source = image
    self.cost_per_tree_per_month.content=cptpm
    self.no_of_trees_available.content=trees_available
    self.rental_duration.selected_value=period_chosen
    self.total_cost.content=total
    self.button_callback = button_callback

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_callback(self.farmer_name.content.lower())

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def rental_duration_change(self, **event_args):
    """This method is called when an item is selected"""
    pass




