import marblex
import time

client = marblex.Client()

while True:

    nkt = client.get_NKT()
    nka = client.get_NKA()

    print("NKT : {}$, Percent: {}".format(nkt.USD, nkt.percent))
    print("NKA : {}$, Percent: {}".format(nka.USD, nka.percent))

    """
    NKT : 1.47$, Percent: -4.22 %
    NKA : 3.56$, Percent: +1.61 %
    """

    time.sleep(5)
