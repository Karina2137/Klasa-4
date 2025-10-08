plik = open("dane.txt", "r")
nominaly = list(map(int, plik.readline().split()))
kwoty = list(map(int, plik.readlines()))
plik.close()
print(nominaly)
print(kwoty)

najmniej_nominalow=100
kwoty_najmniej_nominalow=[]
for kwota in kwoty:
    kw = kwota
    ilosc_nominalow = 0
    for nominal in nominaly:
        ilosc = (kw//nominal)
        ilosc_nominalow+=ilosc
        kw = kw % nominal
    print(ilosc_nominalow, kwota)
    if ilosc_nominalow<najmniej_nominalow:
        najmniej_nominalow=ilosc_nominalow
        kwoty_najmniej_nominalow.append(kwota)
print(kwoty_najmniej_nominalow)

