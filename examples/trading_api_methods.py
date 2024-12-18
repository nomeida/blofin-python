import sys
import os
from datetime import datetime, timedelta

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from blofin.client import BloFinClient
from blofin.constants import MARGIN_MODES, POSITION_MODES, POSITION_SIDES, ORDER_SIDES, ORDER_TYPES, ORDER_STATES

# Replace these with your actual API credentials
API_KEY    = ""
API_SECRET = ""
PASSPHRASE = ""

# Replace with a valid instrument ID for your tests
TEST_INST_ID = 'BTC-USDT'

def test_trading_api():
    client = BloFinClient(API_KEY, API_SECRET, PASSPHRASE)


    # # Test get_futures_account_balance (Endpoint: /api/v1/account/balance)
    # print("Testing get_futures_account_balance:")
    # balance = client.trading.get_futures_account_balance()
    # print(balance)
    # print()


    # # Test get_positions (Endpoint: /api/v1/account/positions)
    # print("Testing get_positions:")
    # positions = client.trading.get_positions(inst_id='BTC-USDT')
    # print(positions)
    # print()


    # # Test get_margin_mode (Endpoint: /api/v1/account/margin-mode)
    # print("Testing get_margin_mode:")
    # margin_mode = client.trading.get_margin_mode()
    # print(margin_mode)
    # print()


    # # Test set_margin_mode (Endpoint: /api/v1/account/set-margin-mode)
    # print("Testing set_margin_mode:")
    # set_margin = client.trading.set_margin_mode(margin_mode='cross')
    # print(set_margin)
    # print()


    # # Test get_position_mode (Endpoint: /api/v1/account/position-mode)
    # print("Testing get_position_mode:")
    # position_mode = client.trading.get_position_mode()
    # print(position_mode)
    # print()


    # # Test set_position_mode (Endpoint: /api/v1/account/set-position-mode)
    # print("Testing set_position_mode:")
    # set_position = client.trading.set_position_mode(position_mode="long_short_mode")
    # print(set_position)
    # print()


    # # Test get_multiple_leverage (Endpoint: /api/v1/account/batch-leverage-info)
    # print("Testing get_multiple_leverage:")
    # leverage_info = client.trading.get_multiple_leverage(inst_id="BTC-USDT,ETH-USDT,SOL-USDT", margin_mode="isolated")
    # print(leverage_info)
    # print()


    # # Test set_leverage (Endpoint: /api/v1/account/set-leverage)
    # print("Testing set_leverage:")
    # set_leverage = client.trading.set_leverage(inst_id="BTC-USDT", leverage=15, margin_mode="cross", position_side="net")
    # print(set_leverage)
    # print()



    # # Test place_order (Endpoint: /api/v1/trade/order)
    # print("Testing place_order:")
    # order = client.trading.place_order(
    #     inst_id      = "ETH-USDT",
    #     margin_mode  = "isolated",
    #     position_side= "net",
    #     side         = "buy",
    #     order_type   = "market",
    #     price        = 50000, #Price is irrelevant when using market order, but we need to provide a value anyways
    #     size         = 1
    # )
    # print(order)
    # print()

    
    # # Assuming the order was placed successfully, use its ID for subsequent tests
    # order_id = order['orderId']

    # # Test cancel_order (Endpoint: /api/v1/trade/cancel-order)
    # print("Testing cancel_order:")
    # cancel_order = client.trading.cancel_order(inst_id="ETH-USDT", order_id="order_id_here")
    # print(cancel_order)
    # print()


    # # Test close_positions (Endpoint: /api/v1/trade/close-position)
    # print("Testing close_positions:")
    # close_pos = client.trading.close_positions(inst_id="ETH-USDT", margin_mode="isolated", position_side="net")
    # print(close_pos)
    # print()


    # # Test place_multiple_orders (Endpoint: /api/v1/trade/batch-orders)
    # print("Testing place_multiple_orders:")
    # multiple_orders = client.trading.place_multiple_orders([
    #     {
    #         'instId'       : "ETH-USDT",
    #         'marginMode'   : "isolated",
    #         'positionSide' : "net",
    #         'side'         : "buy",
    #         'orderType'    : "limit",
    #         'price'        : 2390,
    #         'size'         : 2
    #     },
    #     {
    #         'instId'       : "ETH-USDT",
    #         'marginMode'   : "isolated",
    #         'positionSide' : "net",
    #         'side'         : "buy",
    #         'orderType'    : "limit",
    #         'price'        : 2320,
    #         'size'         : 1
    #     }
    # ])
    # print(multiple_orders)
    # print()


    # # Test get_active_orders (Endpoint: /api/v1/trade/orders-pending)
    # print("Testing get_active_orders:")
    # active_orders = client.trading.get_active_orders(inst_id="ETH-USDT", order_type="limit", state="live", limit=5)
    # print(active_orders)
    # print()


    # # Test cancel_multiple_orders (Endpoint: /api/v1/trade/cancel-batch-orders)
    # print("Testing cancel_multiple_orders:")
    # cancel_multiple = client.trading.cancel_multiple_orders([
    #     {'instId': "ETH-USDT", 'orderId': "order_id_1"},
    #     {'instId': "ETH-USDT", 'orderId': "order_id_2"},
    #     {'instId': "ETH-USDT", 'orderId': "order_id_3"},
    #     # Add more order IDs as needed
    # ])
    # print(cancel_multiple)
    # print()


    # # Test place_tpsl_order (Endpoint: /api/v1/trade/order-tpsl)
    # print("Testing place_tpsl_order:")
    # tpsl_order = client.trading.place_tpsl_order(
    #     inst_id             = "ETH-USDT",
    #     margin_mode         = "isolated",
    #     position_side       = "net",
    #     side                = "buy",
    #     tp_trigger_price    = 2380,
    #     tp_order_price      = 2450,
    #     sl_trigger_price    = 2410,
    #     sl_order_price      = 2369,
    #     size                = 2
    # )
    # print(tpsl_order)
    # print()


    # # Test get_active_tpsl_orders (Endpoint: /api/v1/trade/orders-tpsl-pending)
    # print("Testing get_active_tpsl_orders:")
    # active_tpsl = client.trading.get_active_tpsl_orders(inst_id="ETH-USDT", limit=5)
    # print(active_tpsl)
    # print()


    # # Test cancel_tpsl_order (Endpoint: /api/v1/trade/cancel-tpsl)
    # print("Testing cancel_tpsl_order:")
    # cancel_tpsl = client.trading.cancel_tpsl_order(inst_id="ETH-USDT", tpsl_id="12754158")
    # print(cancel_tpsl)
    # print()


    # # Test get_order_history (Endpoint: /api/v1/trade/orders-history)
    # print("Testing get_order_history:")
    # order_history = client.trading.get_order_history(inst_id="ETH-USDT", order_type="limit", state="", limit=5)
    # print(order_history)
    # print()

    # Get TPSL order history
    print("Testing get_tpsl_order_history:")
    tpsl_history = client.trading.get_tpsl_order_history(limit=50)
    print(tpsl_history)
    print()

    # Get trade history
    print("Testing get_trade_history:")
    trades = client.trading.get_trade_history(begin="1697026383085")
    print(trades)
    print()

    # Get valid price range
    print("Testing get_trade_order_price_range:")
    price_range = client.trading.get_trade_order_price_range(inst_id="BTC-USDT", side="buy")
    print(price_range)
    print()

if __name__ == "__main__":
    test_trading_api()