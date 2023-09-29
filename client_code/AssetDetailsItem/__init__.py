# Import the necessary modules
from anvil import Form, HtmlPanel
from .AssetItemNoButton import AssetItemNoButton  # Import your custom component

class MyForm(Form):
    def __init__(self, **properties):
        self.init_components(**properties)
        
    def add_asset_item(self, farmer_name, location, cptpm, trees_available, rental_duration, total):
        # Create a new instance of AssetItemNoButton component
        asset_item = AssetItemNoButton()
        
        # Set the properties of the component
        asset_item.farmer_name = farmer_name
        asset_item.location = location
        asset_item.cptpm = cptpm
        asset_item.trees_available = trees_available
        asset_item.rental_duration = rental_duration
        asset_item.total = total
        
        # Add the component to an HtmlPanel on the form
        self.html_panel.add_component(asset_item)

