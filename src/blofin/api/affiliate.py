from ..utils import send_request, filter_none_params
from ..constants import (
    AFFILIATE_BASIC_INFO_ENDPOINT, AFFILIATE_REFERRAL_CODE_ENDPOINT, AFFILIATE_INVITEES_ENDPOINT,
    AFFILIATE_SUB_INVITEES_ENDPOINT, AFFILIATE_SUB_AFFILIATES_ENDPOINT, AFFILIATE_INVITEES_DAILY_ENDPOINT,
    AFFILIATE_MAX_LIMIT
)

from ..exceptions import (
    BloFinAPIException, BloFinRequestException, BloFinParameterException,
    BloFinAuthException, BloFinOrderException, BloFinPositionException,
    BloFinBalanceException
)

class AffiliateAPI:
    def __init__(self, client):
        self.client = client

    def get_basic_info(self):
        return send_request('GET', AFFILIATE_BASIC_INFO_ENDPOINT, self.client.auth, authenticate=True)

    def get_referral_code(self):
        return send_request('GET', AFFILIATE_REFERRAL_CODE_ENDPOINT, self.client.auth, authenticate=True)

    def get_invitees(self, uid=None, after=None, before=None, begin=None, end=None, limit=None):
        if limit and limit > AFFILIATE_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {AFFILIATE_MAX_LIMIT}")
        params = filter_none_params(uid=uid, after=after, before=before, begin=begin, end=end, limit=limit)
        return send_request('GET', AFFILIATE_INVITEES_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_sub_invitees(self, uid=None, after=None, before=None, sub_affiliate_uid=None, sub_affiliate_level=None, begin=None, end=None, limit=None):
        if limit and limit > AFFILIATE_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {AFFILIATE_MAX_LIMIT}")
        params = filter_none_params(
            uid=uid, after=after, before=before, subAffiliateUid=sub_affiliate_uid,
            subAffiliateLevel=sub_affiliate_level, begin=begin, end=end, limit=limit
        )
        return send_request('GET', AFFILIATE_SUB_INVITEES_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_sub_affiliates(self, after=None, before=None, sub_affiliate_uid=None, sub_affiliate_level=None, begin=None, end=None, limit=None):
        if limit and limit > AFFILIATE_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {AFFILIATE_MAX_LIMIT}")
        params = filter_none_params(
            after=after, before=before, subAffiliateUid=sub_affiliate_uid,
            subAffiliateLevel=sub_affiliate_level, begin=begin, end=end, limit=limit
        )
        return send_request('GET', AFFILIATE_SUB_AFFILIATES_ENDPOINT, self.client.auth, params=params, authenticate=True)

    def get_invitees_daily(self, uid=None, after=None, before=None, begin=None, end=None, limit=None):
        if limit and limit > AFFILIATE_MAX_LIMIT:
            raise BloFinParameterException(f"Limit must be less than or equal to {AFFILIATE_MAX_LIMIT}")
        params = filter_none_params(uid=uid, after=after, before=before, begin=begin, end=end, limit=limit)
        return send_request('GET', AFFILIATE_INVITEES_DAILY_ENDPOINT, self.client.auth, params=params, authenticate=True)