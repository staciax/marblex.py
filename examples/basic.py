import asyncio
import time

from marblex import Marblex

mbx = Marblex()

async def main() -> None:

    async with mbx:
        while True:

            nkt = await mbx.get_territe_token()
            nka = await mbx.get_asterite_token()

            print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
            print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

            # NKT : 1.47$, Percent: -4.22 %
            # NKA : 3.56$, Percent: +1.61 %

            time.sleep(5)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
