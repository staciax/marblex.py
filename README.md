# marblex.py
 A library to get various cryptocurrency prices from the marblex API.

## Installation

- ```pip install marblex.py```

## Quick Example
```python

import marblex

nkt = marblex.get_nkt()
nka = marblex.get_nka()

print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

# NKT : 1.47$, Percent: -4.22 %
# NKA : 3.56$, Percent: +1.61 %
```
## Client Example
```python
import marblex
import time

client = marblex.Client()

while True:
    
    nkt = client.get_NKT()
    nka = client.get_NKA()
    
    print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
    print(f"NKA : {nka.USD}$, Percent: {nka.percent}")
    
    # NKT : 1.47$, Percent: -4.22 %
    # NKA : 3.56$, Percent: +1.61 %
    
    time.sleep(5)
```

## License
MIT

## inspired by
- [marblex](https://github.com/syntaxp/marblex) by [syntaxp](https://github.com/syntaxp)