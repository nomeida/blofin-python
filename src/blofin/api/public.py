from typing import Optional
from ..utils import send_request, filter_none_params
from ..constants import (
    PUBLIC_INSTRUMENTS_ENDPOINT,
    PUBLIC_TICKERS_ENDPOINT,
    PUBLIC_ORDER_BOOK_ENDPOINT,
    PUBLIC_TRADES_ENDPOINT,
    PUBLIC_MARK_PRICE_ENDPOINT,
    PUBLIC_FUNDING_RATE_ENDPOINT,
    PUBLIC_FUNDING_RATE_HISTORY_ENDPOINT,
    PUBLIC_CANDLESTICKS_ENDPOINT,
    INST_TYPE_SWAP,
    BAR_INTERVALS,
    ORDER_BOOK_MAX_SIZE,
    TRADES_MAX_LIMIT,
    FUNDING_RATE_HISTORY_MAX_LIMIT,
    CANDLESTICK_MAX_LIMIT
)

from ..exceptions import BloFinParameterException

class PublicAPI:
    def __init__(self, client):
        self.client = client

    def get_instruments(self, inst_type: Optional[str] = None):
        if inst_type and inst_type not in [INST_TYPE_SWAP]:
            raise BloFinParameterException(f"Invalid inst_type. Must be one of {INST_TYPE_SWAP}")
        params = filter_none_params(instType=inst_type)
        return send_request('GET', PUBLIC_INSTRUMENTS_ENDPOINT, self.client.auth, params=params)

    def get_tickers(self, inst_id: Optional[str] = None):
        params = filter_none_params(instId=inst_id)
        return send_request('GET', PUBLIC_TICKERS_ENDPOINT, self.client.auth, params=params)

    def get_order_book(self, inst_id: str, size: Optional[int] = None):
        if size and size > ORDER_BOOK_MAX_SIZE:
            raise BloFinParameterException(f"Size must be less than or equal to {ORDER_BOOK_MAX_SIZE}")
        params = filter_none_params(instId=inst_id, size=size)
        return send_request('GET', PUBLIC_ORDER_BOOK_ENDPOINT, self.client.auth, params=params)

    def get_trades(self, inst_id: str, limit: Optional[int] = None):
        if limit and limit > TRADES_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {TRADES_MAX_LIMIT}")
        params = filter_none_params(instId=inst_id, limit=limit)
        return send_request('GET', PUBLIC_TRADES_ENDPOINT, self.client.auth, params=params)

    def get_mark_price(self, inst_id: str):
        params = {'instId': inst_id}
        return send_request('GET', PUBLIC_MARK_PRICE_ENDPOINT, self.client.auth, params=params)

    def get_funding_rate(self, inst_id: str):
        params = {'instId': inst_id}
        return send_request('GET', PUBLIC_FUNDING_RATE_ENDPOINT, self.client.auth, params=params)

    def get_funding_rate_history(self, inst_id: str, before: Optional[str] = None, after: Optional[str] = None, limit: Optional[int] = None):
        if limit and limit > FUNDING_RATE_HISTORY_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {FUNDING_RATE_HISTORY_MAX_LIMIT}")
        params = filter_none_params(instId=inst_id, before=before, after=after, limit=limit)
        return send_request('GET', PUBLIC_FUNDING_RATE_HISTORY_ENDPOINT, self.client.auth, params=params)

    def get_candlesticks(self, inst_id: str, bar: Optional[str] = None, after: Optional[str] = None, before: Optional[str] = None, limit: Optional[int] = None):
        if bar and bar not in BAR_INTERVALS:
            raise BloFinParameterException(f"Invalid bar. Must be one of {', '.join(BAR_INTERVALS)}")
        if limit and limit > CANDLESTICK_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {CANDLESTICK_MAX_LIMIT}")
        params = filter_none_params(instId=inst_id, bar=bar, after=after, before=before, limit=limit)
        return send_request('GET', PUBLIC_CANDLESTICKS_ENDPOINT, self.client.auth, params=params)