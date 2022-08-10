from typing import TypedDict

class MBX(TypedDict):
    previousClosePriceMinor: str
    percentMinor: str
    volumeMinor: str
    priceMajor: str
    lastVolumeUpdated: str
    lastPreviousClosePriceUpdated: str
    previousClosePriceMajor: str
    volumeMajor: str
    counter: str
    percentMajor: str
    priceMinor: str
    lastPriceUpdated: str

class USD(TypedDict):
    previousClosePriceMinor: str
    percentMinor: str
    priceMajor: str
    lastPreviousClosePriceUpdated: str
    previousClosePriceMajor: str
    counter: str
    percentMajor: str
    priceMinor: str
    lastPriceUpdated: str

class Currencies(TypedDict):
    MBX: MBX
    USD: USD

class Coin(TypedDict):
    resultCode: str
    message: str
    tokenCode: str
    currencies: Currencies
