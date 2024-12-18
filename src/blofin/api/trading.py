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

    def get_tpsl_order_history(self, inst_id: Optional[str] = None, tpsl_id: Optional[str] = None, 
                              client_order_id: Optional[str] = None, state: Optional[str] = None,
                              after: Optional[str] = None, before: Optional[str] = None, 
                              limit: Optional[int] = None):
        """
        Retrieve a list of all TP/SL orders under the current account.
        
        Args:
            inst_id (str, optional): Instrument ID, e.g. BTC-USDT
            tpsl_id (str, optional): TP/SL order ID
            client_order_id (str, optional): Client-supplied ID
            state (str, optional): Order state (live, effective, canceled, order_failed)
            after (str, optional): Pagination of data to return records earlier than the requested tpslId
            before (str, optional): Pagination of data to return records newer than the requested tpslId
            limit (int, optional): Number of results per request. Maximum is 100, default is 20
            
        Returns:
            dict: TPSL order history data
        """
        valid_states = ['live', 'effective', 'canceled', 'order_failed']
        if state and state not in valid_states:
            raise BloFinParameterException(f"Invalid state. Must be one of: {', '.join(valid_states)}")
        
        params = filter_none_params(
            instId=inst_id,
            tpslId=tpsl_id,
            clientOrderId=client_order_id,
            state=state,
            after=after,
            before=before,
            limit=limit
        )
        return send_request('GET', TRADE_ORDERS_TPSL_HISTORY_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_trade_history(self, inst_id: Optional[str] = None, order_id: Optional[str] = None,
                         after: Optional[str] = None, before: Optional[str] = None,
                         begin: Optional[str] = None, end: Optional[str] = None,
                         limit: Optional[int] = None):
        """
        Retrieve recently-filled transaction details.
        
        Args:
            inst_id (str, optional): Instrument ID, e.g. BTC-USDT
            order_id (str, optional): Order ID
            after (str, optional): Pagination of data to return records earlier than the requested tradeId
            before (str, optional): Pagination of data to return records newer than the requested tradeId
            begin (str, optional): Filter with a begin timestamp (Unix timestamp in milliseconds)
            end (str, optional): Filter with an end timestamp (Unix timestamp in milliseconds)
            limit (int, optional): Number of results per request. Maximum is 100, default is 20
            
        Returns:
            dict: Trade history data
        """
        params = filter_none_params(
            instId=inst_id,
            orderId=order_id,
            after=after,
            before=before,
            begin=begin,
            end=end,
            limit=limit
        )
        return send_request('GET', TRADE_FILLS_HISTORY_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_trade_order_price_range(self, inst_id: str, side: str):
        """
        Query price limit range for an instrument.
        
        Args:
            inst_id (str): Instrument ID, e.g. BTC-USDT
            side (str): Order side ('buy' or 'sell')
            
        Returns:
            dict: Price range data containing maximum and minimum prices
        """
        if side not in ORDER_SIDES:
            raise BloFinParameterException(f"Invalid side. Must be one of: {', '.join(ORDER_SIDES)}")
        
        params = {
            'instId': inst_id,
            'side': side
        }
        return send_request('GET', TRADE_ORDER_PRICE_RANGE_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def place_algo_order(self, inst_id: str, margin_mode: str, position_side: str, 
                          side: str, size: Union[int, float], order_type: str = 'trigger',
                          order_price: Optional[float] = None, client_order_id: Optional[str] = None,
                          reduce_only: Optional[bool] = None, broker_id: Optional[str] = None,
                          trigger_price: Optional[float] = None,
                          trigger_price_type: Optional[str] = None,
                          attach_algo_orders: Optional[List[dict]] = None) -> dict:
        """
        Place an algorithmic order.

        Args:
            inst_id (str): Instrument ID, e.g. BTC-USDT
            margin_mode (str): Margin mode ('cross' or 'isolated')
            position_side (str): Position side ('net', 'long', or 'short')
            side (str): Order side ('buy' or 'sell')
            size (Union[int, float]): Order size. Use -1 for entire position
            order_type (str, optional): Algo type (default: 'trigger')
            order_price (float, optional): Order price. Use -1 for market price
            client_order_id (str, optional): Client-supplied ID
            reduce_only (bool, optional): Whether order can only reduce position size
            broker_id (str, optional): Broker ID
            trigger_price (float, optional): Trigger price for trigger orders
            trigger_price_type (str, optional): Type of trigger price (e.g., 'last')
            attach_algo_orders (List[dict], optional): Attached TP/SL orders info

        Returns:
            dict: Order placement result containing algo_id and client_order_id
        """
        if margin_mode not in MARGIN_MODES:
            raise BloFinParameterException(f"Invalid margin_mode. Must be one of: {', '.join(MARGIN_MODES)}")
        if position_side not in POSITION_SIDES:
            raise BloFinParameterException(f"Invalid position_side. Must be one of: {', '.join(POSITION_SIDES)}")
        if side not in ORDER_SIDES:
            raise BloFinParameterException(f"Invalid side. Must be one of: {', '.join(ORDER_SIDES)}")
        if order_type not in ALGO_ORDER_TYPES:
            raise BloFinParameterException(f"Invalid order_type. Must be one of: {', '.join(ALGO_ORDER_TYPES)}")
        if trigger_price_type and trigger_price_type not in TRIGGER_PRICE_TYPES:
            raise BloFinParameterException(f"Invalid trigger_price_type. Must be one of: {', '.join(TRIGGER_PRICE_TYPES)}")

        data = {
            'instId': inst_id,
            'marginMode': margin_mode,
            'positionSide': position_side,
            'side': side,
            'size': str(size),
            'orderType': order_type
        }

        if order_price is not None:
            data['orderPrice'] = str(order_price)
        if client_order_id is not None:
            data['clientOrderId'] = client_order_id
        if reduce_only is not None:
            data['reduceOnly'] = str(reduce_only).lower()
        if broker_id is not None:
            data['brokerId'] = broker_id
        if trigger_price is not None:
            data['triggerPrice'] = str(trigger_price)
        if trigger_price_type is not None:
            data['triggerPriceType'] = trigger_price_type
        if attach_algo_orders is not None:
            data['attachAlgoOrders'] = attach_algo_orders

        return send_request('POST', TRADE_ORDER_ALGO_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def cancel_algo_order(self, inst_id: str, algo_id: str, client_order_id: Optional[str] = None) -> dict:
        """
        Cancel an algorithmic order.

        Args:
            inst_id (str): Instrument ID
            algo_id (str): Algo order ID
            client_order_id (str, optional): Client-supplied ID

        Returns:
            dict: Cancellation result
        """
        data = {
            'instId': inst_id,
            'algoId': algo_id
        }
        if client_order_id:
            data['clientOrderId'] = client_order_id

        return send_request('POST', TRADE_CANCEL_ALGO_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def get_active_algo_orders(self, inst_id: Optional[str] = None, algo_id: Optional[str] = None,
                             client_order_id: Optional[str] = None, after: Optional[str] = None,
                             before: Optional[str] = None, limit: Optional[int] = None,
                             order_type: str = 'trigger') -> dict:
        """
        Retrieve a list of untriggered algo orders under the current account.

        Args:
            inst_id (str, optional): Instrument ID
            algo_id (str, optional): Algo order ID
            client_order_id (str, optional): Client-supplied ID
            after (str, optional): Pagination of data to return records earlier than the requested algoId
            before (str, optional): Pagination of data to return records newer than the requested algoId
            limit (int, optional): Number of results per request (default: 20, max: 100)
            order_type (str, optional): Algo type (default: 'trigger')

        Returns:
            dict: Active algo orders data
        """
        if order_type not in ALGO_ORDER_TYPES:
            raise BloFinParameterException(f"Invalid order_type. Must be one of: {', '.join(ALGO_ORDER_TYPES)}")
        if limit is not None and (not isinstance(limit, int) or limit <= 0 or limit > ALGO_MAX_LIMIT):
            raise BloFinParameterException(f"Limit must be a positive integer not exceeding {ALGO_MAX_LIMIT}")

        params = filter_none_params(
            instId=inst_id,
            algoId=algo_id,
            clientOrderId=client_order_id,
            after=after,
            before=before,
            limit=limit,
            orderType=order_type
        )
        return send_request('GET', TRADE_ORDERS_ALGO_PENDING_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_algo_order_history(self, inst_id: Optional[str] = None, algo_id: Optional[str] = None,
                             client_order_id: Optional[str] = None, state: Optional[str] = None,
                             after: Optional[str] = None, before: Optional[str] = None,
                             limit: Optional[int] = None, order_type: str = 'trigger') -> dict:
        """
        Retrieve a list of all algo orders under the current account.

        Args:
            inst_id (str, optional): Instrument ID
            algo_id (str, optional): Algo order ID
            client_order_id (str, optional): Client-supplied ID
            state (str, optional): Order state ('live', 'effective', 'canceled', 'order_failed')
            after (str, optional): Pagination of data to return records earlier than the requested algoId
            before (str, optional): Pagination of data to return records newer than the requested algoId
            limit (int, optional): Number of results per request (default: 20, max: 100)
            order_type (str, optional): Algo type (default: 'trigger')

        Returns:
            dict: Algo order history data
        """
        if order_type not in ALGO_ORDER_TYPES:
            raise BloFinParameterException(f"Invalid order_type. Must be one of: {', '.join(ALGO_ORDER_TYPES)}")
        if limit is not None and (not isinstance(limit, int) or limit <= 0 or limit > ALGO_MAX_LIMIT):
            raise BloFinParameterException(f"Limit must be a positive integer not exceeding {ALGO_MAX_LIMIT}")
        
        valid_states = ['live', 'effective', 'canceled', 'order_failed']
        if state and state not in valid_states:
            raise BloFinParameterException(f"Invalid state. Must be one of: {', '.join(valid_states)}")

        params = filter_none_params(
            instId=inst_id,
            algoId=algo_id,
            clientOrderId=client_order_id,
            state=state,
            after=after,
            before=before,
            limit=limit,
            orderType=order_type
        )
        return send_request('GET', TRADE_ORDERS_ALGO_HISTORY_ENDPOINT, self.client.auth, params=params, authenticate=True)