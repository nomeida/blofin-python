import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from blofin.client import BloFinClient

# Replace these with your actual API credentials
API_KEY    = ""
API_SECRET = ""
PASSPHRASE = ""

def test_user_api():
    client = BloFinClient(API_KEY, API_SECRET, PASSPHRASE)

    # Test get_api_key_info (Endpoint: /api/v1/user/query-apikey)
    print("Testing get_api_key_info:")
    api_key_info = client.user.get_api_key_info()
    print(api_key_info)
    print()

if __name__ == "__main__":
    test_user_api()