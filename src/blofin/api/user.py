from ..utils import send_request
from ..constants import USER_API_KEY_INFO_ENDPOINT

from ..exceptions import (
    BloFinAPIException, BloFinRequestException, BloFinParameterException,
    BloFinAuthException, BloFinOrderException, BloFinPositionException,
    BloFinBalanceException
)

class UserAPI:
    def __init__(self, client):
        self.client = client

    def get_api_key_info(self):
        return send_request('GET', USER_API_KEY_INFO_ENDPOINT, self.client.auth, authenticate=True)