import marblex

nkt = marblex.get_nkt()
nka = marblex.get_nka()

print(f"NKT : {nkt.USD}$, Percent: {nkt.percent}")
print(f"NKA : {nka.USD}$, Percent: {nka.percent}")

# NKT : 1.47$, Percent: -4.22 %
# NKA : 3.56$, Percent: +1.61 %
