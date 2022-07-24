from __future__ import annotations

import datetime
from typing import Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .types.marblex import (
        Coin as CoinPayload
    )
    from .types.exchange import (
        LoremboardExchange as LoremboardExchangePayload
    )
    from .client import Client

__all__ = ('Coin', 'Exchange',)


class Coin:

    """ Coin """

    def __init__(self, *, client: Client, data: CoinPayload) -> None:
        self._client = client
        self.token_code: str = data['tokenCode']
        self._update(data)

    def _update(self, data: CoinPayload) -> None:
        self._currencies = data['currencies']
        self._usd = self._currencies['USD']
        self._percent_major: str = self._usd['percentMajor']
        self._percent_minor: str = self._usd['percentMinor']
        self._price_major: str = self._usd['priceMajor']
        self._price_minor: str = self._usd['priceMinor']
        self._last_price_updated: str = self._usd['lastPriceUpdated']

    def __repr__(self) -> str:
        return f'<Coin token_code={self.token_code!r} THB={self.THB!r} USD={self.USD!r} percent={self.percent!r}>'

    def __eq__(self, other) -> bool:
        return isinstance(other, Coin) and self.token_code == other.token_code and self._currencies == other._currencies

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @property
    def _exchange(self) -> Optional[Exchange]:
        """ Return the Exchange object for this Coin. """
        return self._client.get_exchange()

    @property
    def percent(self) -> float:
        """ Return the percent of the price change. """

        # https://github.com/syntaxp/marblex/blob/main/mbx.py
        # thanks to syntaxp for the idea

        coin = f'_{self.token_code.lower()}_percent'
        _current_percent = getattr(self._client, coin)
        e_percent = "{:.2f} %".format(float(self._percent_major + "." + self._percent_minor))

        if not e_percent.startswith("-"):
            setattr(self._client, coin, "+" + e_percent)
        else:
            if getattr(self._client, coin) == "-0.00 %":
                setattr(self._client, coin, "+0.00 %")
            else:
                e_percent = "{:.2f} %".format(float(self._percent_major + "." + self._percent_minor))
                setattr(self._client, coin, e_percent)

        return getattr(self._client, coin)

    @property
    def _average_price(self) -> float:
        """ Return the average price of the coin. """
        return float(self._price_major + "." + self._price_minor)

    @property
    def THB(self) -> str:
        """ Return the price of the coin in THB. """
        return "{:.2f}".format(float("{:.4f}".format((self._average_price * self._exchange.THB))))

    @property
    def USD(self) -> str:
        """ Return the price of the coin in USD. """
        return "{:.2f}".format(float("{:.4f}".format((self._average_price * self._exchange.USD))))


class Exchange:

    """ Return the price of the coin in THB. """

    def __init__(self, *, client: Client, data: Optional[LoremboardExchangePayload]) -> None:
        self._client = client
        self._update(data)

    def _update(self, data: Optional[LoremboardExchangePayload]) -> None:
        self._base: str = data['base']
        self._timestamp: int = data['timestamp']
        self._date: str = data['date']
        self._success: bool = data['success']
        self._rates: Dict[str, float] = data['rates']

    def __repr__(self) -> str:
        attrs = [
            ('base', self.base),
            ('USD', self.USD),
            ('THB', self.THB),
            ('updated_at', self.updated_at),
        ]
        joined = ' '.join('%s=%r' % t for t in attrs)
        return f'<{self.__class__.__name__} {joined}>'

    def __eq__(self, other) -> bool:
        return isinstance(other, Exchange) and self._timestamp == other._timestamp and self._rates == other._rates

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @property
    def base(self) -> str:
        """ Return the base currency. """
        return self._base

    @property
    def updated_at(self) -> datetime.datetime:
        """ Return the datetime of the last update. """
        return datetime.datetime.fromtimestamp(self._timestamp)

    @property
    def THB(self) -> float:
        """ Return the price of the coin in THB. """
        return self._rates['THB']

    @property
    def USD(self) -> float:
        """ Return the price of the coin in USD. """
        return self._rates['USD']
