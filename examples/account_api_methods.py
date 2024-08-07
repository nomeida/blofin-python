import sys
import os
from decimal import Decimal

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.blofin.client import BloFinClient

# Replace these with your actual API credentials
API_KEY    = ""
API_SECRET = ""
PASSPHRASE = ""

def test_account_api():
    client = BloFinClient(API_KEY, API_SECRET, PASSPHRASE)

    # Test get_account_balance (Endpoint: /api/v1/asset/balances)
    print("Testing get_account_balance:")
    account_balance = client.account.get_account_balance()
    print(account_balance)
    print()

    # Test get_positions (Endpoint: /api/v1/account/positions)
    print("Testing get_positions:")
    positions = client.account.get_positions()
    print(positions)
    print()

    # Test get_balance (Endpoint: /api/v1/asset/balance)
    print("Testing get_balance:")
    balance = client.account.get_balance(account_type='funding', currency='USDT')
    print(balance)
    print()

    # Test funds_transfer (Endpoint: /api/v1/asset/transfer)
    print("Testing funds_transfer:")
    transfer = client.account.funds_transfer(currency='USDT', amount=1.0, from_account='futures', to_account='funding', client_id='test_transfer_1')
    print(transfer)
    print()

    # Test get_funds_transfer_history (Endpoint: /api/v1/asset/transfer-history)
    print("Testing get_funds_transfer_history:")
    transfer_history = client.account.get_funds_transfer_history(currency='USDT', limit=5)
    print(transfer_history)
    print()

    # Test get_withdraw_history (Endpoint: /api/v1/asset/withdraw-history)
    print("Testing get_withdraw_history:")
    withdraw_history = client.account.get_withdraw_history(currency='USDT', limit=5)
    print(withdraw_history)
    print()

    # Test get_deposit_history (Endpoint: /api/v1/asset/deposit-history)
    print("Testing get_deposit_history:")
    deposit_history = client.account.get_deposit_history(currency='USDT', limit=5)
    print(deposit_history)
    print()

if __name__ == "__main__":
    test_account_api()