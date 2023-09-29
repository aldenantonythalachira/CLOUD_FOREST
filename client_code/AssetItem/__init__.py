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
  def __init__(self, farmer_name, location, image, cptpm, trees_available, rental_duration,total,button_click, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.farmer_name.content = "FARMER NAME : "+farmer_name
    self.location.content = "LOCATION : "+location
    self.image_tree.source = image
    self.cost_per_tree_per_month.content="CPTPM : SGD "+str(cptpm)
    self.no_of_trees_available.content="TREES AVAILABLE : "+str(trees_available)
    self.rental_duration.content="RENTAL DURATION : "+str(rental_duration)+" months"
    self.total_cost.content="TOTAL : SGD "+str(total)
    self.button_click=button_click
  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass




