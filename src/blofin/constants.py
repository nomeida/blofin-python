# API URLs
REST_API_URL = 'https://openapi.blofin.com'
WEBSOCKET_PUBLIC_URL = 'wss://openapi.blofin.com/ws/public'
WEBSOCKET_PRIVATE_URL = 'wss://openapi.blofin.com/ws/private'

### API Endpoints

# Account endpoints
ACCOUNT_BALANCE_ENDPOINT            = '/api/v1/asset/balances'
ACCOUNT_TRANSFER_ENDPOINT           = '/api/v1/asset/transfer'
ACCOUNT_BILLS_ENDPOINT              = '/api/v1/asset/bills'
ACCOUNT_WITHDRAWAL_HISTORY_ENDPOINT = '/api/v1/asset/withdrawal-history'
ACCOUNT_DEPOSIT_HISTORY_ENDPOINT    = '/api/v1/asset/deposit-history'

# Trade endpoints
FUTURES_ACCOUNT_BALANCE_ENDPOINT      = '/api/v1/account/balance'
ACCOUNT_POSITIONS_ENDPOINT            = '/api/v1/account/positions'
ACCOUNT_MARGIN_MODE_ENDPOINT          = '/api/v1/account/margin-mode'
ACCOUNT_SET_MARGIN_MODE_ENDPOINT      = '/api/v1/account/set-margin-mode'
ACCOUNT_POSITION_MODE_ENDPOINT        = '/api/v1/account/position-mode'
ACCOUNT_SET_POSITION_MODE_ENDPOINT    = '/api/v1/account/set-position-mode'
ACCOUNT_BATCH_LEVERAGE_INFO_ENDPOINT  = '/api/v1/account/batch-leverage-info'
ACCOUNT_SET_LEVERAGE_ENDPOINT         = '/api/v1/account/set-leverage'
TRADE_ORDER_ENDPOINT                  = '/api/v1/trade/order'
TRADE_BATCH_ORDERS_ENDPOINT           = '/api/v1/trade/batch-orders'
TRADE_ORDER_TPSL_ENDPOINT             = '/api/v1/trade/order-tpsl'
TRADE_CANCEL_ORDER_ENDPOINT           = '/api/v1/trade/cancel-order'
TRADE_CANCEL_BATCH_ORDERS_ENDPOINT    = '/api/v1/trade/cancel-batch-orders'
TRADE_CANCEL_TPSL_ENDPOINT            = '/api/v1/trade/cancel-tpsl'
TRADE_ORDERS_PENDING_ENDPOINT         = '/api/v1/trade/orders-pending'
TRADE_ORDERS_TPSL_PENDING_ENDPOINT    = '/api/v1/trade/orders-tpsl-pending'
TRADE_CLOSE_POSITION_ENDPOINT         = '/api/v1/trade/close-position'
TRADE_ORDERS_HISTORY_ENDPOINT         = '/api/v1/trade/orders-history'
TRADE_ORDERS_TPSL_HISTORY_ENDPOINT    = '/api/v1/trade/orders-tpsl-history'
TRADE_FILLS_HISTORY_ENDPOINT          = '/api/v1/trade/fills-history'

# Public API Endpoints
PUBLIC_INSTRUMENTS_ENDPOINT           = '/api/v1/market/instruments'
PUBLIC_TICKERS_ENDPOINT               = '/api/v1/market/tickers'
PUBLIC_ORDER_BOOK_ENDPOINT            = '/api/v1/market/books'
PUBLIC_TRADES_ENDPOINT                = '/api/v1/market/trades'
PUBLIC_MARK_PRICE_ENDPOINT            = '/api/v1/market/mark-price'
PUBLIC_FUNDING_RATE_ENDPOINT          = '/api/v1/market/funding-rate'
PUBLIC_FUNDING_RATE_HISTORY_ENDPOINT  = '/api/v1/market/funding-rate-history'
PUBLIC_CANDLESTICKS_ENDPOINT          = '/api/v1/market/candles'

# Affiliate API endpoints
AFFILIATE_BASIC_INFO_ENDPOINT     = '/api/v1/affiliate/basic'
AFFILIATE_REFERRAL_CODE_ENDPOINT  = '/api/v1/affiliate/referral-code'
AFFILIATE_INVITEES_ENDPOINT       = '/api/v1/affiliate/invitees'
AFFILIATE_SUB_INVITEES_ENDPOINT   = '/api/v1/affiliate/sub-invitees'
AFFILIATE_SUB_AFFILIATES_ENDPOINT = '/api/v1/affiliate/sub-affiliates'
AFFILIATE_INVITEES_DAILY_ENDPOINT = '/api/v1/affiliate/invitees/daily'

# Algo trading endpoints
TRADE_ORDER_ALGO_ENDPOINT = '/api/v1/trade/order-algo'
TRADE_CANCEL_ALGO_ENDPOINT = '/api/v1/trade/cancel-algo'
TRADE_ORDERS_ALGO_PENDING_ENDPOINT = '/api/v1/trade/orders-algo-pending'
TRADE_ORDERS_ALGO_HISTORY_ENDPOINT = '/api/v1/trade/orders-algo-history'

# User API endpoints
USER_API_KEY_INFO_ENDPOINT = '/api/v1/user/query-apikey'

# Miscellaneous
SERVER_TIME_ENDPOINT = '/api/v1/public/time'


# Account types
ACCOUNT_TYPE_FUNDING = "funding"
ACCOUNT_TYPE_FUTURES = "futures"
ACCOUNT_TYPE_COPY_TRADING = "copy_trading"
ACCOUNT_TYPE_EARN = "earn"
ACCOUNT_TYPE_SPOT = "spot"

ACCOUNT_TYPES = [
    ACCOUNT_TYPE_FUNDING,
    ACCOUNT_TYPE_FUTURES,
    ACCOUNT_TYPE_COPY_TRADING,
    ACCOUNT_TYPE_EARN,
    ACCOUNT_TYPE_SPOT
]

# Withdrawal states
WITHDRAWAL_STATE_WAITING = "0"
WITHDRAWAL_STATE_WITHDRAWING = "1"
WITHDRAWAL_STATE_FAILED = "2"
WITHDRAWAL_STATE_APPROVED = "3"
WITHDRAWAL_STATE_CANCELED = "4"
WITHDRAWAL_STATE_KYT = "6"
WITHDRAWAL_STATE_PROCESSING = "7"

WITHDRAWAL_STATES = [
    WITHDRAWAL_STATE_WAITING,
    WITHDRAWAL_STATE_WITHDRAWING,
    WITHDRAWAL_STATE_FAILED,
    WITHDRAWAL_STATE_APPROVED,
    WITHDRAWAL_STATE_CANCELED,
    WITHDRAWAL_STATE_KYT,
    WITHDRAWAL_STATE_PROCESSING
]

# Deposit states
DEPOSIT_STATE_PENDING = "0"
DEPOSIT_STATE_DONE = "1"
DEPOSIT_STATE_FAILED = "2"
DEPOSIT_STATE_KYT = "3"

DEPOSIT_STATES = [
    DEPOSIT_STATE_PENDING,
    DEPOSIT_STATE_DONE,
    DEPOSIT_STATE_FAILED,
    DEPOSIT_STATE_KYT
]

# Candlestick bar intervals
BAR_1M = "1m"
BAR_3M = "3m"
BAR_5M = "5m"
BAR_15M = "15m"
BAR_30M = "30m"
BAR_1H = "1H"
BAR_2H = "2H"
BAR_4H = "4H"
BAR_6H = "6H"
BAR_8H = "8H"
BAR_12H = "12H"
BAR_1D = "1D"
BAR_3D = "3D"
BAR_1W = "1W"
BAR_1MO = "1M"

BAR_INTERVALS = [
    BAR_1M, BAR_3M, BAR_5M, BAR_15M, BAR_30M,
    BAR_1H, BAR_2H, BAR_4H, BAR_6H, BAR_8H, BAR_12H,
    BAR_1D, BAR_3D, BAR_1W, BAR_1MO
]

# Instrument types
INST_TYPE_SWAP = "SWAP"

INSTRUMENT_TYPES = [INST_TYPE_SWAP]

# Order side constants
ORDER_SIDE_BUY = "buy"
ORDER_SIDE_SELL = "sell"

ORDER_SIDES = [ORDER_SIDE_BUY, ORDER_SIDE_SELL]

# Order type constants
ORDER_TYPE_MARKET = "market"
ORDER_TYPE_LIMIT = "limit"
ORDER_TYPE_POST_ONLY = "post_only"
ORDER_TYPE_FOK = "fok"
ORDER_TYPE_IOC = "ioc"

ORDER_TYPES = [ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, ORDER_TYPE_POST_ONLY, ORDER_TYPE_FOK, ORDER_TYPE_IOC]

ALGO_ORDER_TYPES = ['trigger']  # Add more as they become available
TRIGGER_PRICE_TYPES = ['last']  # Add more as they become available

# Margin mode constants
MARGIN_MODE_CROSS = "cross"
MARGIN_MODE_ISOLATED = "isolated"

MARGIN_MODES = [MARGIN_MODE_CROSS, MARGIN_MODE_ISOLATED]

# Position side constants
POSITION_SIDE_LONG = "long"
POSITION_SIDE_SHORT = "short"
POSITION_SIDE_NET = "net"

POSITION_SIDES = [POSITION_SIDE_LONG, POSITION_SIDE_SHORT, POSITION_SIDE_NET]

# Position mode constants
POSITION_MODE_NET = "net_mode"
POSITION_MODE_LONG_SHORT = "long_short_mode"

POSITION_MODES = [POSITION_MODE_NET, POSITION_MODE_LONG_SHORT]

# Order state constants
ORDER_STATE_LIVE = "live"
ORDER_STATE_CANCELED = "canceled"
ORDER_STATE_FILLED = "filled"
ORDER_STATE_PARTIALLY_FILLED = "partially_filled"

ORDER_STATES = [ORDER_STATE_LIVE, ORDER_STATE_CANCELED, ORDER_STATE_FILLED, ORDER_STATE_PARTIALLY_FILLED]

# Sub-affiliate levels
SUB_AFFILIATE_LEVEL_2 = "2"
SUB_AFFILIATE_LEVEL_3 = "3"
SUB_AFFILIATE_LEVEL_4 = "4"

SUB_AFFILIATE_LEVELS = [SUB_AFFILIATE_LEVEL_2, SUB_AFFILIATE_LEVEL_3, SUB_AFFILIATE_LEVEL_4]

# Default and maximum limit for pagination
DEFAULT_LIMIT = 20
MAX_LIMIT = 100

# Order book max size
ORDER_BOOK_MAX_SIZE = 100

# Trades max limit
TRADES_MAX_LIMIT = 100

# Funding rate history max limit
FUNDING_RATE_HISTORY_MAX_LIMIT = 100

# Candlestick max limit
CANDLESTICK_MAX_LIMIT = 1440

# Affiliate max limit
AFFILIATE_MAX_LIMIT = 100

# Account max limit
ACCOUNT_MAX_LIMIT = 100

# Trading max order size
TRADING_MAX_ORDER_SIZE = 1000

# Algo trading max order size
ALGO_MAX_LIMIT = 100