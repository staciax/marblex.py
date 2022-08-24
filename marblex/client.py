from __future__ import annotations

import logging

from .http import HTTPClient, HTTPSyncClient
from .models import *

from typing import Type, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self
    from types import TracebackType

_log = logging.getLogger(__name__)

__all__ = ('Client', 'Marblex', 'SyncClient', 'MarblexSync')

class Client:

    """ Marblex API Wrapper Client """

    def __init__(self, ssl: bool = False):

        # http client
        self.__http = HTTPClient(ssl=ssl)

        # cache stuff
        self._nkt_percent: str = ''
        self._nka_percent: str = ''
        self._itu_percent: str = ''

        # config stuff
        self._closed: bool = False

    async def get_territe_token(self) -> Optional[Coin]:
        """ Get NKT Coin. """
        data = await self.__http.fetch_territe_token()
        coin = Coin(client=self, data=data)
        await coin.get_exchange()
        return coin

    async def get_asterite_token(self) -> Optional[Coin]:
        """ Get NKA Coin. """
        data = await self.__http.fetch_asterite_token()
        coin = Coin(client=self, data=data)
        await coin.get_exchange()
        return coin

    async def get_inetrium_token(self) -> Optional[Coin]:
        """ Get ITU Coin. """
        data = await self.__http.fetch_inetrium_token()
        coin = Coin(client=self, data=data)
        await coin.get_exchange()
        return coin

    async def get_exchange(self) -> Optional[Exchange]:
        """ Return the Exchange object. """
        data = await self.__http.fetch_loremboard()
        return Exchange(client=self, data=data)

    async def __aenter__(self) -> Self:
        _log.info('Opened the Marblex client.')
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if not self.is_closed():
            await self.close()

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        await self.__http.close()
        _log.info('Closed the Marblex client.')

    def is_closed(self) -> bool:
        return self._closed

class SyncClient(Client):

    """ Marblex API Wrapper Client (Sync) """

    def __init__(self, ssl: bool = False):
        super().__init__()
        self.__http = HTTPSyncClient(ssl=ssl)

    def get_territe_token(self) -> Optional[Coin]:
        """ Get NKT Coin. """
        data = self.__http.fetch_territe_token()
        coin = Coin(client=self, data=data)
        return coin

    def get_asterite_token(self) -> Optional[Coin]:
        """ Get NKA Coin. """
        data = self.__http.fetch_asterite_token()
        coin = Coin(client=self, data=data)
        return coin

    def get_inetrium_token(self) -> Optional[Coin]:
        """ Get ITU Coin. """
        data = self.__http.fetch_inetrium_token()
        coin = Coin(client=self, data=data)
        return coin

    def get_exchange(self) -> Optional[Exchange]:
        """ Return the Exchange object. """
        data = self.__http.fetch_loremboard()
        return Exchange(client=self, data=data)

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self.__http.close()
        _log.info('Closed the Marblex client.')

    def is_closed(self) -> bool:
        return self._closed


Marblex = Client
MarblexSync = SyncClient