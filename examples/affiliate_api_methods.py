import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.blofin.client import BloFinClient

# Replace these with your actual API credentials
API_KEY    = ""
API_SECRET = ""
PASSPHRASE = ""

def test_affiliate_api():
    client = BloFinClient(API_KEY, API_SECRET, PASSPHRASE)

    # Test get_basic_info (Endpoint: /api/v1/affiliate/basic)
    print("Testing get_basic_info:")
    basic_info = client.affiliate.get_basic_info()
    print(basic_info)
    print()

    # Test get_referral_code (Endpoint: /api/v1/affiliate/referral-code)
    print("Testing get_referral_code:")
    referral_code = client.affiliate.get_referral_code()
    print(referral_code)
    print()

    # Test get_invitees (Endpoint: /api/v1/affiliate/invitees)
    print("Testing get_invitees:")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    invitees = client.affiliate.get_invitees(
        uid=None,
        after=None,
        before=None,
        begin=int(start_date.timestamp() * 1000),
        end=int(end_date.timestamp() * 1000),
        limit=5
    )
    print(invitees)
    print()

    # Test get_sub_invitees (Endpoint: /api/v1/affiliate/sub-invitees)
    print("Testing get_sub_invitees:")
    sub_invitees = client.affiliate.get_sub_invitees(
        uid=None,
        after=None,
        before=None,
        sub_affiliate_uid=None,
        sub_affiliate_level=None,
        begin=int(start_date.timestamp() * 1000),
        end=int(end_date.timestamp() * 1000),
        limit=5
    )
    print(sub_invitees)
    print()

    # Test get_sub_affiliates (Endpoint: /api/v1/affiliate/sub-affiliates)
    print("Testing get_sub_affiliates:")
    sub_affiliates = client.affiliate.get_sub_affiliates(
        after=None,
        before=None,
        sub_affiliate_uid=None,
        sub_affiliate_level=None,
        begin=int(start_date.timestamp() * 1000),
        end=int(end_date.timestamp() * 1000),
        limit=5
    )
    print(sub_affiliates)
    print()

    # Test get_invitees_daily (Endpoint: /api/v1/affiliate/invitees/daily)
    print("Testing get_invitees_daily:")
    invitees_daily = client.affiliate.get_invitees_daily(
        uid=None,
        after=None,
        before=None,
        begin=int(start_date.timestamp() * 1000),
        end=int(end_date.timestamp() * 1000),
        limit=5
    )
    print(invitees_daily)
    print()

if __name__ == "__main__":
    test_affiliate_api()