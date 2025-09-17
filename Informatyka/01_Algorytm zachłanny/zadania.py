plik = open("nominaly.txt", "r")
nominaly = list(map(int, plik.read().split()))
plik.close()

#zad.1
print(nominaly)
print("Z ilu wydać resztę?")
kwota = int(input())
n = len(nominaly)
ile = [0]*n
for i in range (n):
    ile[i] = (kwota//nominaly[i])
    kwota %= nominaly[i]
print(ile)

for i in range (n):
    if ile[i]>0:
        print(ile[i]," x ",nominaly[i])

#zad.5
wartosc = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, }
rzymska = input()
liczba = 0
ostatnia = rzymska[-1]
for i in range(len(rzymska)-1):
    litera = rzymska[i]
    nastepna = rzymska[i+1]
    if wartosc[litera] >= wartosc[nastepna]: liczba += wartosc[litera]
    else: liczba -= wartosc[litera]
liczba+=wartosc[ostatnia]
print(liczba)
