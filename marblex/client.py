from __future__ import annotations

import logging
from .http import HTTPClient
from .models import *

from typing import Optional

_log = logging.getLogger(__name__)

__all__ = ('Client',)

class Client:

    """ Marblex API Wrapper Client """

    def __init__(self):
        self._http = HTTPClient()
        self._nkt_percent: str = ''
        self._nka_percent: str = ''

    def get_NKA(self) -> Optional[Coin]:
        """ Return the NKA Coin. """
        data = self._http.fetch_NKA()
        if data is None:
            return None
        return Coin(client=self, data=data)

    def get_NKT(self) -> Optional[Coin]:
        """ Return the NKT Coin. """
        data = self._http.fetch_NKT()
        if data is None:
            return None
        return Coin(client=self, data=data)

    def get_exchange(self) -> Optional[Exchange]:
        """ Return the Exchange object. """
        data = self._http.fetch_loremboard()
        if data is None:
            return None
        return Exchange(client=self, data=data)

    def close(self) -> None:
        """ Close the client. """
        self._http.close()

    def __enter__(self) -> Client:
        _log.debug('Entering context manager')
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()
        return None

    def __del__(self) -> None:
        self.close()
        return None
