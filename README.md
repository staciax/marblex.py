# marblex.py
 An Asynchronous Marblex API Wrapper for Python

## Installation
Windows: <br>
```
$ pip install -U marblex.py
```
Linux/MacOS:
```
$ python3 -m pip install -U marblex.py
```

## Asynchronous Example:
```python
import asyncio
from marblex import Marblex

mbx = Marblex()

async def main():

    async with mbx:
        nkt = await mbx.get_territe_token()
        nka = await mbx.get_asterite_token()

        print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
        print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
## Synchronous Example:
```python
from marblex import MarblexSync

mbx = MarblexSync()

nkt = mbx.get_territe_token()
nka = mbx.get_asterite_token()
itu = mbx.get_inetrium_token()

print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
print(f"NKA : {nka.USD}$, Percent: {nka.percent}")
print(f"ITU : {itu.USD}$, Percent: {itu.percent}")

>>> NKT : 1.47$, Percent: -4.22 %
>>> NKA : 3.56$, Percent: +1.61 %
>>> ITU : 0.13$, Percent: -0.59 %
```
## License
MIT

## inspired by
- [marblex](https://github.com/syntaxp/marblex) by [syntaxp](https://github.com/syntaxp)