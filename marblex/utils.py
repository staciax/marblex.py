from .client import Client
from .models import Coin

__all__ = ('get_nkt', 'get_nka')

def get_nkt() -> Coin:
    """ get the NKT coin without the client """
    with Client() as client:
        return client.get_NKT()

def get_nka() -> Coin:
    """ get the NKA coin without the client """
    with Client() as client:
        return client.get_NKA()
