from __future__ import annotations

import sys
import aiohttp
import requests
import logging
import urllib3

from urllib.parse import urlencode

from . import __version__, utils
from .utils import MISSING

from typing import Any, ClassVar, Coroutine, Optional, TypeVar, TYPE_CHECKING

# disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if TYPE_CHECKING:

    T = TypeVar('T')
    Response = Coroutine[Any, Any, T]

    from .types.marblex import (
        Coin as CoinPayload
    )
    from .types.exchange import (
        LoremboardExchange as LoremboardExchangePayload
    )

_log = logging.getLogger(__name__)

__all__ = ('HTTPClient',)
class Route:

    BASE_MARBLEX_URL: ClassVar[str] = 'https://ninokuni.marblex.io/api'
    BASE_LOREM_URL: ClassVar[str] = 'https://api.loremboard.finance/api/v1'

    def __init__(
        self,
        method: str,
        path: str,
        endpoint: Optional[str] = "mbx",
        **parameters: Any
    ) -> None:
        self.method: str = method
        self.path: str = path

        url = ''
        if endpoint == "mbx":
            url = self.BASE_MARBLEX_URL + path
        elif endpoint == "lorem":
            url = self.BASE_LOREM_URL + path

        if parameters:
            url = url + '?' + urlencode(parameters)
        self.url: str = url

class HTTPClient:

    """Represents an HTTP client sending HTTP requests to the Marblex API."""

    def __init__(self, ssl: bool = False) -> None:
        self._ssl = ssl
        self.__session: aiohttp.ClientSession = MISSING

        user_agent = 'Marblex.py (https://github.com/staciax/marblex.py {0}) Python/{1[0]}.{1[1]} aiohttp/{2}'
        self.user_agent: str = user_agent.format(__version__, sys.version_info, aiohttp.__version__)

    async def request(self, route: Route, **kwargs: Any) -> Any:
        method = route.method
        url = route.url

        if self.__session is MISSING:
            self.__session = aiohttp.ClientSession()

        # headers
        kwargs['headers'] = {
            'User-Agent': self.user_agent,
        }

        # verify ssl
        kwargs['verify_ssl'] = self._ssl

        async with self.__session.request(method, url, **kwargs) as response:

            if response.status == 200:
                _log.debug(f'HTTP request status: {response.status}')
                data = await utils.json_or_text(response)
                return data
            else:
                _log.error(f'HTTP request failed: {response.url}')
                raise Exception(f'HTTP request failed: {response.url}')

            # TODO: error handling

    # marblex endpoints

    def fetch_territe_token(self) -> Response[CoinPayload]:
        return self.request(Route('GET', '/price', tokenType='NKT'))

    def fetch_asterite_token(self) -> Response[CoinPayload]:
        return self.request(Route('GET', '/price', tokenType='NKA'))

    def fetch_inetrium_token(self) -> Response[CoinPayload]:
        return self.request(Route('GET', '/price', tokenType='ITU'))

    # exchange endpoints

    def fetch_loremboard(self) -> Response[LoremboardExchangePayload]:
        return self.request(Route('GET', '/dashboard/fiat/latest', endpoint="lorem"))

    async def close(self) -> None:
        _log.debug('Closing HTTP client')
        await self.__session.close()
        self.__session = MISSING

class HTTPSyncClient(HTTPClient):

    """Represents an HTTP client sending HTTP requests to the Marblex API."""

    def __init__(self, ssl: bool = False) -> None:
        super().__init__(ssl)
        self.__session: requests.Session = MISSING

    def request(self, route: Route, **kwargs: Any) -> Any:
        method = route.method
        url = route.url

        if self.__session is MISSING:
            self.__session = requests.Session()

        # headers
        kwargs['headers'] = {
            'User-Agent': self.user_agent,
        }

        # verify ssl
        kwargs['verify'] = self._ssl

        response = self.__session.request(method, url, **kwargs)

        if response.status_code == 200:
            _log.debug(f'HTTP request status: {response.status_code}')
            data = response.json()
            return data
        else:
            _log.error(f'HTTP request failed: {response.url}')
            raise Exception(f'HTTP request failed: {response.url}')

    def close(self) -> None:
        _log.debug('Closing HTTP client')
        self.__session.close()
        self.__session = MISSING