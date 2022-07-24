from __future__ import annotations

import requests
import logging
from typing import Any, TYPE_CHECKING

_log = logging.getLogger(__name__)

__all__ = ('HTTPClient',)

if TYPE_CHECKING:
    from .types.marblex import (
        Coin as CoinPayload
    )
    from .types.exchange import (
        LoremboardExchange as LoremboardExchangePayload
    )

class HTTPClient:

    """Represents an HTTP client sending HTTP requests to the Marblex API."""

    BASE_URL = 'https://ninokuni.marblex.io/api'
    PRICE_TOKEN = '/price?tokenType='

    def __init__(self) -> None:
        self.__session = requests.Session()

    def request(self, method: str, url: str, **kwargs: Any) -> Any:
        with self.__session.request(method, url, **kwargs) as response:
            if response.status_code == 200:
                _log.debug(f'HTTP request successful: {response.url}')
                return response.json()
            else:
                _log.error(f'HTTP request failed: {response.url}')
                return None

            # todo error handling

    def fetch_NKA(self) -> CoinPayload:
        return self.request('GET', self.BASE_URL + self.PRICE_TOKEN + 'NKA')

    def fetch_NKT(self) -> CoinPayload:
        return self.request('GET', self.BASE_URL + self.PRICE_TOKEN + 'NKT')

    def fetch_loremboard(self) -> LoremboardExchangePayload:
        return self.request('GET', 'https://api.loremboard.finance/api/v1/dashboard/fiat/latest')

    def close(self) -> None:
        _log.debug('Closing HTTP client')
        self.__session.close()
