import time
from marblex import Marblex

mbx = Marblex()

def main() -> None:

    while True:

        nkt = mbx.get_NKT()
        nka = mbx.get_NKA()

        print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
        print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

        # NKT : 1.47$, Percent: -4.22 %
        # NKA : 3.56$, Percent: +1.61 %

        time.sleep(5)

if __name__ == '__main__':
    with mbx:
        main()
