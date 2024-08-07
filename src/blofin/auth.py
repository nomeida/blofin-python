import hmac
import base64
import time
import json
import hashlib
import uuid
import urllib
from hashlib import sha256
from .utils import get_server_time

class Auth:
    def __init__(self, api_key, api_secret, passphrase, use_server_time=False):
        self.API_KEY = api_key
        self.API_SECRET = api_secret
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time

    def get_timestamp(self):
        if self.use_server_time:
            return get_server_time()
        return str(int(round(time.time() * 1000)))

    def generate_signature(self, timestamp, method, request_path, body='', nonce=''):
        body = "" if method == "GET" else json.dumps(body)
        
        prehash_string = f"{request_path}{method.upper()}{timestamp}{nonce}{body}"
        
        signature = hmac.new(self.API_SECRET.encode(), prehash_string.encode(), hashlib.sha256)
        hexdigest = signature.hexdigest()
        hexdigest_to_bytes = hexdigest.encode()
        return base64.b64encode(hexdigest_to_bytes).decode()

    def get_headers(self, request_path: str, method: str = 'GET', body: dict = {}):
        timestamp = self.get_timestamp()
        nonce = uuid.uuid4().hex
        
        params = {}  # Add this if you need to handle query parameters
        url_params_string = urllib.parse.urlencode(params)
        url_params_string = "?" + url_params_string if url_params_string else ""
        
        headers = {
            'ACCESS-KEY': self.API_KEY,
            'ACCESS-SIGN': self.generate_signature(timestamp, method, request_path + url_params_string, body, nonce),
            'ACCESS-TIMESTAMP': timestamp,
            'ACCESS-PASSPHRASE': self.PASSPHRASE,
            'Content-Type': 'application/json',
            'ACCESS-NONCE': nonce
        }
        return headers