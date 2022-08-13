import time

from marblex import MarblexSync

mbx = MarblexSync()

def main() -> None:

    while True:

        nkt = mbx.get_territe_token()
        nka = mbx.get_asterite_token()
        itu = mbx.get_inetrium_token()

        print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
        print(f"NKA : {nka.USD}$, Percent: {nka.percent}")
        print(f"ITU : {itu.USD}$, Percent: {itu.percent}")

        # NKT : 1.47$, Percent: -4.22 %
        # NKA : 3.56$, Percent: +1.61 %
        # ITU : 0.13$, Percent: -0.59 %

        time.sleep(5)

if __name__ == '__main__':
    main()
