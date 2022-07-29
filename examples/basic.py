import time
from marblex import Marblex
mbx = Marblex()

while True:

    nkt = mbx.get_NKT()
    nka = mbx.get_NKA()

    print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
    print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

    # NKT : 1.47$, Percent: -4.22 %
    # NKA : 3.56$, Percent: +1.61 %

    time.sleep(5)
