import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Assets import Assets
from ..MyAssets import MyAssets

urls = {"home": Home, "assets": Assets, "my-assets": MyAssets}
