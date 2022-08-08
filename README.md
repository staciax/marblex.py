# marblex.py
 An Asynchronous Marblex API Wrapper for Python

## Installation
Windows: <br>
```
$ pip install -U marblex.py
```
Linux/MacOS:
```
$  python3 -m pip install -U marblex.py
```


## Example Usage:
```python
import asyncio
from marblex import Marblex

mbx = Marblex()

async def main():

    async with mbx:
        nkt = await mbx.get_NKT()
        nka = await mbx.get_NKA()

        print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
        print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## License
MIT

## inspired by
- [marblex](https://github.com/syntaxp/marblex) by [syntaxp](https://github.com/syntaxp)