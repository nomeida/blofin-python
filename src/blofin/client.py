from blofin.constants import REST_API_URL, WEBSOCKET_PUBLIC_URL, WEBSOCKET_PRIVATE_URL
from blofin.exceptions import (
    BloFinAPIException, BloFinRequestException, BloFinParameterException,
    BloFinAuthException, BloFinOrderException, BloFinPositionException,
    BloFinBalanceException
)
from blofin.api.public import PublicAPI
from blofin.api.account import AccountAPI
from blofin.api.trading import TradingAPI
from blofin.api.affiliate import AffiliateAPI
from blofin.api.user import UserAPI
from blofin.auth import Auth
from blofin.utils import check_auth_credentials

# Rest of the client.py content...

class BloFinClient:
    def __init__(self, api_key=None, api_secret=None, passphrase=None, use_server_time=False):
        self.auth = Auth(api_key, api_secret, passphrase, use_server_time)
        self.use_server_time = use_server_time
        self.authenticated = check_auth_credentials(api_key, api_secret, passphrase)

        if not self.authenticated:
            print("Warning: API credentials not provided. Some methods requiring authentication will not be accessible.")

        self.public    = PublicAPI(self)
        self.account   = AccountAPI(self)
        self.trading   = TradingAPI(self)
        self.affiliate = AffiliateAPI(self)
        self.user      = UserAPI(self)

    def get_server_time(self):
        return self.public.get_server_time()