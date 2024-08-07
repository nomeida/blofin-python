# BloFin API SDK

A Python SDK for the BloFin API, providing easy access to BloFin's trading platform functionalities.

## Installation

You can install the BloFin API SDK using pip:

```bash
pip install blofin
```

## Quick Start

Here's a quick example of how to use the BloFin API SDK:

```python
from blofin import BloFinClient

# Initialize the client
client = BloFinClient(api_key='your_api_key', api_secret='your_api_secret', passphrase='your_passphrase')

# Use the client to interact with different APIs
```

## Usage

The SDK provides access to various APIs:

### Public API

The Public API allows you to access public market data without authentication.

```python
# Get instruments
instruments = client.public.get_instruments(inst_type='SWAP')

# Get tickers
tickers = client.public.get_tickers(inst_id='BTC-USDT')

# Get order book
order_book = client.public.get_order_book(inst_id='BTC-USDT', size=20)

# Get candlestick data
candles = client.public.get_candlesticks(inst_id='BTC-USDT', bar='1m', limit=100)
```

### Account API

The Account API allows you to manage your account information and perform account-related operations.

```python
# Get account balance
balance = client.account.get_balance(account_type='futures')

# Transfer funds
transfer = client.account.funds_transfer(
    currency='USDT',
    amount=100,
    from_account='funding',
    to_account='futures'
)

# Get deposit history
deposits = client.account.get_deposit_history(currency='USDT', limit=10)
```

### Trading API

The Trading API allows you to place and manage orders, as well as retrieve trading-related information.

```python
# Place an order
order = client.trading.place_order(
    inst_id='BTC-USDT',
    margin_mode='cross',
    position_side='long',
    side='buy',
    order_type='limit',
    price=30000,
    size=0.01
)

# Get open positions
positions = client.trading.get_positions(inst_id='BTC-USDT')

# Cancel an order
cancel = client.trading.cancel_order(inst_id='BTC-USDT', order_id='123456')

# Get order history
history = client.trading.get_order_history(inst_id='BTC-USDT', limit=50)
```

## Important Notes

1. **API Credentials**: To use authenticated endpoints, you need to provide your BloFin API credentials (API key, API secret, and passphrase) when initializing the client.

2. **Rate Limiting**: Be aware of BloFin's rate limits for API requests. Exceeding these limits may result in temporary blocks or account suspension.

3. **Error Handling**: The SDK uses custom exceptions to handle various error scenarios. Always wrap your API calls in try-except blocks to handle potential errors gracefully.

4. **Pagination**: Some methods that return lists of items (e.g., order history) support pagination. Use the `before`, `after`, and `limit` parameters to navigate through large result sets.

5. **Server Time**: If you experience timestamp-related issues, you can initialize the client with `use_server_time=True` to use BloFin's server time for requests.

## Contributing

Contributions to the BloFin API SDK are welcome! Please refer to the project's GitHub repository for information on how to contribute, report issues, or request features.

## To Do:

- Websocket support

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This SDK is not officially associated with BloFin.