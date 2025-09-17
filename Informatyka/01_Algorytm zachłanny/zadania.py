plik = open("nominaly.txt", "r")
nominaly = list(map(int, plik.read().split()))
plik.close()

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
