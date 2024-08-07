from typing import Optional
from ..utils import send_request, filter_none_params
from ..constants import (
    ACCOUNT_BALANCE_ENDPOINT,
    ACCOUNT_TRANSFER_ENDPOINT,
    ACCOUNT_BILLS_ENDPOINT,
    ACCOUNT_WITHDRAWAL_HISTORY_ENDPOINT,
    ACCOUNT_DEPOSIT_HISTORY_ENDPOINT,
    ACCOUNT_TYPES,
    WITHDRAWAL_STATES,
    DEPOSIT_STATES,
    MAX_LIMIT
)

from ..exceptions import BloFinParameterException

class AccountAPI:
    def __init__(self, client):
        self.client = client

    def get_balance(self, account_type: str, currency: Optional[str] = None):
        if account_type not in ACCOUNT_TYPES:
            raise BloFinParameterException(f"Invalid account_type. Must be one of {', '.join(ACCOUNT_TYPES)}")
        
        params = filter_none_params(accountType=account_type, currency=currency)
        return send_request('GET', ACCOUNT_BALANCE_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def funds_transfer(self, currency: str, amount: float, from_account: str, to_account: str, client_id: Optional[str] = None):
        if from_account not in ACCOUNT_TYPES:
            raise BloFinParameterException(f"Invalid from_account. Must be one of {', '.join(ACCOUNT_TYPES)}")
        if to_account not in ACCOUNT_TYPES:
            raise BloFinParameterException(f"Invalid to_account. Must be one of {', '.join(ACCOUNT_TYPES)}")
        
        data = filter_none_params(
            currency=currency,
            amount=str(amount),
            fromAccount=from_account,
            toAccount=to_account,
            clientId=client_id
        )
        return send_request('POST', ACCOUNT_TRANSFER_ENDPOINT, self.client.auth, data=data, authenticate=True)

    def get_funds_transfer_history(self, currency: Optional[str] = None, from_account: Optional[str] = None, 
                                to_account: Optional[str] = None, before: Optional[str] = None, 
                                after: Optional[str] = None, limit: Optional[int] = None):
        if from_account and from_account not in ACCOUNT_TYPES:
            raise BloFinParameterException(f"Invalid from_account. Must be one of {', '.join(ACCOUNT_TYPES)}")
        if to_account and to_account not in ACCOUNT_TYPES:
            raise BloFinParameterException(f"Invalid to_account. Must be one of {', '.join(ACCOUNT_TYPES)}")
        if limit is not None and (not isinstance(limit, int) or limit <= 0 or limit > MAX_LIMIT):
            raise BloFinParameterException(f"Limit must be a positive integer not exceeding {MAX_LIMIT}")
        
        params = filter_none_params(
            currency=currency,
            fromAccount=from_account,
            toAccount=to_account,
            before=before,
            after=after,
            limit=limit
        )
        return send_request('GET', ACCOUNT_BILLS_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_withdraw_history(self, currency: Optional[str] = None, withdraw_id: Optional[str] = None, 
                            tx_id: Optional[str] = None, state: Optional[str] = None, 
                            before: Optional[str] = None, after: Optional[str] = None, 
                            limit: Optional[int] = None):
        if state and state not in WITHDRAWAL_STATES:
            raise BloFinParameterException(f"Invalid state. Must be one of {', '.join(WITHDRAWAL_STATES)}")
        if limit is not None and (not isinstance(limit, int) or limit <= 0 or limit > MAX_LIMIT):
            raise BloFinParameterException(f"Limit must be a positive integer not exceeding {MAX_LIMIT}")
        
        params = filter_none_params(
            currency=currency,
            withdrawId=withdraw_id,
            txId=tx_id,
            state=state,
            before=before,
            after=after,
            limit=limit
        )
        return send_request('GET', ACCOUNT_WITHDRAWAL_HISTORY_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_deposit_history(self, currency: Optional[str] = None, deposit_id: Optional[str] = None, 
                            tx_id: Optional[str] = None, state: Optional[str] = None, 
                            before: Optional[str] = None, after: Optional[str] = None, 
                            limit: Optional[int] = None):
        if state and state not in DEPOSIT_STATES:
            raise BloFinParameterException(f"Invalid state. Must be one of {', '.join(DEPOSIT_STATES)}")
        if limit is not None and (not isinstance(limit, int) or limit <= 0 or limit > MAX_LIMIT):
            raise BloFinParameterException(f"Limit must be a positive integer not exceeding {MAX_LIMIT}")
        
        params = filter_none_params(
            currency=currency,
            depositId=deposit_id,
            txId=tx_id,
            state=state,
            before=before,
            after=after,
            limit=limit
        )
        return send_request('GET', ACCOUNT_DEPOSIT_HISTORY_ENDPOINT, self.client.auth, params=params, authenticate=True)