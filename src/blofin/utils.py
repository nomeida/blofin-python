import requests
from urllib.parse import urlencode
from .exceptions import BloFinRequestException, raise_api_exception, BloFinAuthException
from .constants import REST_API_URL, SERVER_TIME_ENDPOINT

def check_auth_credentials(api_key, api_secret, passphrase):
    return all([api_key, api_secret, passphrase])

def send_request(method, request_path, auth, params=None, data=None, authenticate=False):
    url = REST_API_URL + request_path
    
    if authenticate and not check_auth_credentials(auth.API_KEY, auth.API_SECRET, auth.PASSPHRASE):
        raise BloFinAuthException("API credentials are required for this method. Please provide API key, API secret, and an API passphrase.")

    try:
        if method == 'GET':
            if params:
                full_path = request_path + '?' + urlencode(params)
            else:
                full_path = request_path
            headers = auth.get_headers(full_path, method) if authenticate else {}
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            headers = auth.get_headers(request_path, method, data) if authenticate else {}

            response = requests.post(url, headers=headers, json=data)
        else:
            raise BloFinRequestException(f"Unsupported HTTP method: {method}")

        response.raise_for_status()
        
        if not str(response.status_code).startswith('2'):
            raise_api_exception(response)
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise BloFinRequestException(f"Request failed: {str(e)}")

def get_server_time():
    response = requests.get(f"{REST_API_URL}{SERVER_TIME_ENDPOINT}")
    if response.status_code == 200:
        return int(response.json()['data']['timestamp'])
    else:
        raise Exception("Failed to get server time")

def filter_none_params(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}