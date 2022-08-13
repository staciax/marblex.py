import asyncio
import time

from marblex import Marblex

mbx = Marblex()

async def main() -> None:

    async with mbx:
        while True:

            nkt = await mbx.get_territe_token()
            nka = await mbx.get_asterite_token()
            itu = await mbx.get_inetrium_token()

            print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
            print(f"NKA : {nka.USD}$, Percent: {nka.percent}")
            print(f"ITU : {itu.USD}$, Percent: {itu.percent}")

            # NKT : 1.47$, Percent: -4.22 %
            # NKA : 3.56$, Percent: +1.61 %
            # ITU : 0.13$, Percent: -0.59 %

            time.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
