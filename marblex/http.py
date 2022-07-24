from __future__ import annotations

import requests

from typing import Any, TYPE_CHECKING

__all__ = ('HTTPClient',)

if TYPE_CHECKING:
    from .types.marblex import (
        Coin as CoinPayload
    )
    from .types.exchange import (
        LoremboardExchange as LoremboardExchangePayload
    )

class HTTPClient:

    """ HTTPClient """

    BASE_URL = 'https://ninokuni.marblex.io/api'
    PRICE_TOKEN = '/price?tokenType='

    def __init__(self) -> None:
        self.__session = requests.Session()

    def request(self, method: str, url: str, **kwargs: Any) -> Any:
        with self.__session.request(method, url, **kwargs) as response:
            if response.status_code == 200:
                return response.json()
            else:
                return None

    def fetch_NKA(self) -> CoinPayload:
        return self.request('GET', self.BASE_URL + self.PRICE_TOKEN + 'NKA')

    def fetch_NKT(self) -> CoinPayload:
        return self.request('GET', self.BASE_URL + self.PRICE_TOKEN + 'NKT')

    def fetch_loremboard(self) -> LoremboardExchangePayload:
        return self.request('GET', 'https://api.loremboard.finance/api/v1/dashboard/fiat/latest')

    def close(self) -> None:
        self.__session.close()
