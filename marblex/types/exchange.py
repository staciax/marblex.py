from typing import TypedDict, Dict

class LoremboardExchange(TypedDict):
    success: bool
    timestamp: int
    base: str
    date: str
    rates: Dict[str, float]  # so alot of keys
