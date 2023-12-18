import cloudinary
from cloudinary.api import resource_by_asset_id
from cloudinary.exceptions import Error as CloudinaryError

# Set your Cloudinary configuration
cloudinary.config( 
  cloud_name = "dluqfppiy", 
  api_key = "954876298159228", 
  api_secret = "O8GySsTCpz8pmKB--qhL02P9UCY"
)

# Replace "your_asset_id" with the actual asset ID you want to retrieve information for
asset_id = "d847f1b68b619cf367fdead179e2e5f5"

try:
    # Retrieve resource information by asset ID
    result = resource_by_asset_id(asset_id)

    # Print the result
    print(result)
except CloudinaryError as e:
    print(f"Cloudinary API Error: {e}")
