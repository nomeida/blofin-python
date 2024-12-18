import sys
import os
import time

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from blofin.client import BloFinClient

def test_public_api():
    # Initialize the client without authentication for public endpoints
    client = BloFinClient()

    # Test get_instruments (Endpoint: /api/v1/market/instruments)
    print("Testing get_instruments:")
    instruments = client.public.get_instruments()
    print(instruments)
    print()

    # Test get_tickers (Endpoint: /api/v1/market/tickers)
    print("Testing get_tickers:")
    tickers = client.public.get_tickers(inst_id="BTC-USDT")
    print(tickers)
    print()

    # Test get_order_book (Endpoint: /api/v1/market/order-book)
    print("Testing get_order_book:")
    order_book = client.public.get_order_book(inst_id="BTC-USDT", size=5)
    print(order_book)
    print()

    # Test get_trades (Endpoint: /api/v1/market/trades)
    print("Testing get_trades:")
    trades = client.public.get_trades(inst_id="BTC-USDT", limit=5)
    print(trades)
    print()

    # Test get_mark_price (Endpoint: /api/v1/market/mark-price)
    print("Testing get_mark_price:")
    mark_price = client.public.get_mark_price(inst_id="BTC-USDT")
    print(mark_price)
    print()

    # Test get_funding_rate (Endpoint: /api/v1/market/funding-rate)
    print("Testing get_funding_rate:")
    funding_rate = client.public.get_funding_rate(inst_id="BTC-USDT")
    print(funding_rate)
    print()

    # Test get_funding_rate_history (Endpoint: /api/v1/market/funding-rate-history)
    print("Testing get_funding_rate_history:")
    funding_rate_history = client.public.get_funding_rate_history(inst_id="BTC-USDT", limit=5)
    print(funding_rate_history)
    print()

    # Test get_candlesticks (Endpoint: /api/v1/market/candlesticks)
    print("Testing get_candlesticks:")
    candlesticks = client.public.get_candlesticks(inst_id="BTC-USDT", bar="1D", limit=5)
    print(candlesticks)
    print()

if __name__ == "__main__":
    test_public_api()