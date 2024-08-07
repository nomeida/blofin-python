class BloFinAPIException(Exception):
    def __init__(self, response):
        self.code = 0
        if isinstance(response, str):
            self.message = response
        else:
            try:
                json_res = response.json()
            except ValueError:
                self.message = f'Invalid JSON error message from BloFin: {response.text}'
            else:
                if 'code' in json_res and 'msg' in json_res:
                    self.code = json_res['code']
                    self.message = json_res['msg']
                else:
                    self.message = f'Unknown error format from BloFin: {json_res}'


    def __str__(self):
        return f'BloFinAPIException(code={self.code}): {self.message}'

class BloFinRequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'BloFinRequestException: {self.message}'

class BloFinParameterException(BloFinAPIException):
    """Raised when there's an issue with the parms sent to the API"""
    pass

class BloFinAuthException(BloFinAPIException):
    """Raised when there's an auth issue"""
    pass

class BloFinOrderException(BloFinAPIException):
    """issue related to orders"""
    pass

class BloFinPositionException(BloFinAPIException):
    """issue related to positions"""
    pass

class BloFinBalanceException(BloFinAPIException):
    """raised when theres an issue related to account balance"""
    pass

def raise_api_exception(response):
    code = int(response.json().get('code', 0))
    
    if 152000 <= code < 153000:
        raise BloFinParameterException(response)
    elif 152400 <= code < 152500:
        raise BloFinAuthException(response)
    elif 102000 <= code < 103000:
        raise BloFinOrderException(response)
    elif 103000 <= code < 104000 or 110000 <= code < 111000:
        raise BloFinPositionException(response)
    elif 150000 <= code < 151000:
        raise BloFinBalanceException(response)
    else:
        raise BloFinAPIException(response)