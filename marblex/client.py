from __future__ import annotations

import asyncio
import logging
from .http import HTTPClient
from .models import *

from typing import Type, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self
    from types import TracebackType


_log = logging.getLogger(__name__)

__all__ = ('Client', 'Marblex')

class Client:

    """ Marblex API Wrapper Client """

    def __init__(self):
        self.__http = HTTPClient()
        self._nkt_percent: str = ''
        self._nka_percent: str = ''

        self._loop = asyncio.get_event_loop()
        self._closed: bool = False

    async def get_NKA(self) -> Optional[Coin]:
        """ Return the NKA Coin. """
        data = await self.__http.fetch_NKA()
        coin = Coin(client=self, data=data)
        await coin.get_exchange()
        return coin

    async def get_NKT(self) -> Optional[Coin]:
        """ Return the NKT Coin. """
        data = await self.__http.fetch_NKT()
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

Marblex = Client