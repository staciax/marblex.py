# marblex.py
 A library to get various cryptocurrency prices from the marblex API.

## Installation

- ```pip install marblex.py```

## Example
- basic usage:
```python

import marblex

nkt = marblex.get_nkt()
nka = marblex.get_nka()

print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

# NKT : 1.47$, Percent: -4.22 %
# NKA : 3.56$, Percent: +1.61 %
```
- with client:
```python
import marblex
import time

client = marblex.Client()

while True:
    
    nkt = client.get_NKT()
    print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
    
    # NKT : 1.47$, Percent: -4.22 %
    
    time.sleep(5)
```

## License
MIT

## inspired by
- [marblex](https://github.com/syntaxp/marblex) by [syntaxp](https://github.com/syntaxp)