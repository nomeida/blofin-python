from typing import List, Optional, Union
from ..utils import send_request, filter_none_params
from ..constants import (
    FUTURES_ACCOUNT_BALANCE_ENDPOINT,
    ACCOUNT_POSITIONS_ENDPOINT,
    ACCOUNT_MARGIN_MODE_ENDPOINT,
    ACCOUNT_SET_MARGIN_MODE_ENDPOINT,
    ACCOUNT_POSITION_MODE_ENDPOINT,
    ACCOUNT_SET_POSITION_MODE_ENDPOINT,
    ACCOUNT_BATCH_LEVERAGE_INFO_ENDPOINT,
    ACCOUNT_SET_LEVERAGE_ENDPOINT,
    TRADE_ORDER_ENDPOINT,
    TRADE_BATCH_ORDERS_ENDPOINT,
    TRADE_ORDER_TPSL_ENDPOINT,
    TRADE_CANCEL_ORDER_ENDPOINT,
    TRADE_CANCEL_BATCH_ORDERS_ENDPOINT,
    TRADE_CANCEL_TPSL_ENDPOINT,
    TRADE_ORDERS_PENDING_ENDPOINT,
    TRADE_ORDERS_TPSL_PENDING_ENDPOINT,
    TRADE_CLOSE_POSITION_ENDPOINT,
    TRADE_ORDERS_HISTORY_ENDPOINT,
    TRADE_ORDERS_TPSL_HISTORY_ENDPOINT,
    TRADE_FILLS_HISTORY_ENDPOINT,
    ORDER_SIDES,
    ORDER_TYPES,
    MARGIN_MODES,
    POSITION_SIDES,
    POSITION_MODES,
    ORDER_STATES
)

from ..exceptions import (
    BloFinAPIException,
    BloFinRequestException,
    BloFinParameterException,
    BloFinAuthException,
    BloFinOrderException,
    BloFinPositionException,
    BloFinBalanceException
)

class TradingAPI:
    def __init__(self, client):
        self.client = client

    def get_futures_account_balance(self):
        return send_request('GET', FUTURES_ACCOUNT_BALANCE_ENDPOINT, self.client.auth, authenticate=True)

    def get_positions(self, inst_id: Optional[str] = None):
        params = {'instId': inst_id} if inst_id else {}
        return send_request('GET', ACCOUNT_POSITIONS_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_margin_mode(self):
        return send_request('GET', ACCOUNT_MARGIN_MODE_ENDPOINT, self.client.auth, authenticate=True)

    def set_margin_mode(self, margin_mode: str):
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        data = {'marginMode': margin_mode}
        return send_request('POST', ACCOUNT_SET_MARGIN_MODE_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def get_position_mode(self):
        return send_request('GET', ACCOUNT_POSITION_MODE_ENDPOINT, self.client.auth, authenticate=True)

    def set_position_mode(self, position_mode: str):
        if position_mode not in POSITION_MODES:
            raise BloFinParameterException(f"Invalid position_mode. Must be one of: {', '.join(POSITION_MODES)}")
        data = {'positionMode': position_mode}
        return send_request('POST', ACCOUNT_SET_POSITION_MODE_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def get_multiple_leverage(self, inst_id: str, margin_mode: str):
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        params = {'instId': inst_id, 'marginMode': margin_mode}
        return send_request('GET', ACCOUNT_BATCH_LEVERAGE_INFO_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def set_leverage(self, inst_id: str, leverage: int, margin_mode: str, position_side: Optional[str] = None):
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        if position_side and position_side not in POSITION_SIDES:
            raise BloFinParameterException(f"Invalid position_side. Must be one of: {', '.join(POSITION_SIDES)}")
        data = {
            'instId': inst_id,
            'leverage': leverage,
            'marginMode': margin_mode
        }
        if position_side:
            data['positionSide'] = position_side
        return send_request('POST', ACCOUNT_SET_LEVERAGE_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def place_order(self, inst_id: str, margin_mode: str, position_side: str, side: str, order_type: str, price: float, size: float, **kwargs):
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        if position_side not in POSITION_SIDES:
            raise BloFinParameterException(f"Invalid position_side. Must be one of: {', '.join(POSITION_SIDES)}")
        if side not in ORDER_SIDES:
            raise BloFinParameterException(f"Invalid side. Must be one of: {', '.join(ORDER_SIDES)}")
        if order_type not in ORDER_TYPES:
            raise BloFinParameterException(f"Invalid order_type. Must be one of: {', '.join(ORDER_TYPES)}")
        
        data = {
            'instId': inst_id,
            'marginMode': margin_mode,
            'positionSide': position_side,
            'side': side,
            'orderType': order_type,
            'price': price,
            'size': size,
            **kwargs
        }
        return send_request('POST', TRADE_ORDER_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def place_multiple_orders(self, orders: List[dict]):
        return send_request('POST', TRADE_BATCH_ORDERS_ENDPOINT, self.client.auth, data=orders, authenticate=True)

    def place_tpsl_order(self, inst_id: str, margin_mode: str, position_side: str, side: str, tp_trigger_price: float, tp_order_price: float, sl_trigger_price: float, sl_order_price: float, size: float, **kwargs):
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        if position_side not in POSITION_SIDES:
            raise BloFinParameterException(f"Invalid position_side. Must be one of: {', '.join(POSITION_SIDES)}")
        if side not in ORDER_SIDES:
            raise BloFinParameterException(f"Invalid side. Must be one of: {', '.join(ORDER_SIDES)}")
        
        data = {
            'instId': inst_id,
            'marginMode': margin_mode,
            'positionSide': position_side,
            'side': side,
            'tpTriggerPrice': tp_trigger_price,
            'tpOrderPrice': tp_order_price,
            'slTriggerPrice': sl_trigger_price,
            'slOrderPrice': sl_order_price,
            'size': size,
            **kwargs
        }
        return send_request('POST', TRADE_ORDER_TPSL_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def cancel_order(self, inst_id: str, order_id: str, client_order_id: Optional[str] = None):
        data = {'instId': inst_id, 'orderId': order_id}
        if client_order_id:
            data['clientOrderId'] = client_order_id
        return send_request('POST', TRADE_CANCEL_ORDER_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def cancel_multiple_orders(self, orders: List[dict]):
        return send_request('POST', TRADE_CANCEL_BATCH_ORDERS_ENDPOINT, self.client.auth, data=orders, authenticate=True)

    def cancel_tpsl_order(self, inst_id: str, tpsl_id: str, client_order_id: Optional[str] = None):
        data = {'instId': inst_id, 'tpslId': tpsl_id, 'clientOrderId': client_order_id if client_order_id else ''}
        if client_order_id:
            data['clientOrderId'] = client_order_id
        return send_request('POST', TRADE_CANCEL_TPSL_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def get_active_orders(self, inst_id: Optional[str] = None, order_type: Optional[str] = None, state: Optional[str] = None, after: Optional[str] = None, before: Optional[str] = None, limit: Optional[int] = None):
        if order_type and order_type not in ORDER_TYPES:
            raise BloFinParameterException(f"Invalid order_type. Must be one of: {', '.join(ORDER_TYPES)}")
        if state and state not in ORDER_STATES:
            raise BloFinParameterException(f"Invalid state. Must be one of: {', '.join(ORDER_STATES)}")
        
        params = filter_none_params(instId=inst_id, orderType=order_type, state=state, after=after, before=before, limit=limit)
        return send_request('GET', TRADE_ORDERS_PENDING_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_active_tpsl_orders(self, inst_id: Optional[str] = None, tpsl_id: Optional[str] = None, client_order_id: Optional[str] = None, after: Optional[str] = None, before: Optional[str] = None, limit: Optional[int] = None):
        params = filter_none_params(instId=inst_id, tpslId=tpsl_id, clientOrderId=client_order_id, after=after, before=before, limit=limit)
        return send_request('GET', TRADE_ORDERS_TPSL_PENDING_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def close_positions(self, inst_id: str, margin_mode: str, position_side: str, client_order_id: Optional[str] = None):
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        if position_side not in POSITION_SIDES:
            raise BloFinParameterException(f"Invalid position_side. Must be one of: {', '.join(POSITION_SIDES)}")
        
        data = {
            'instId': inst_id,
            'marginMode': margin_mode,
            'positionSide': position_side
        }
        if client_order_id:
            data['clientOrderId'] = client_order_id
        return send_request('POST', TRADE_CLOSE_POSITION_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def get_order_history(self, inst_id: Optional[str] = None, order_type: Optional[str] = None, state: Optional[str] = None, after: Optional[str] = None, before: Optional[str] = None, begin: Optional[str] = None, end: Optional[str] = None, limit: Optional[int] = None):
        if order_type and order_type not in ORDER_TYPES:
            raise BloFinParameterException(f"Invalid order_type. Must be one of: {', '.join(ORDER_TYPES)}")
        if state and state not in ORDER_STATES:
            raise BloFinParameterException(f"Invalid state. Must be one of: {', '.join(ORDER_STATES)}")
        
        params = filter_none_params(instId=inst_id, orderType=order_type, state=state, after=after, before=before, begin=begin, end=end, limit=limit)
        return send_request('GET', TRADE_ORDERS_HISTORY_ENDPOINT, self.client.auth, params=params, authenticate=True)