# Specifinių funkcijų importavimas su alias
# Užduotis 5:
# Sukurkite Python programą, kuri:
# 1. Importuoja sqrt funkciją iš math modulio su alias sq.
# 2. Apskaičiuoja kvadratinę šaknį iš 625 naudojant sq().
# 3. Išspausdina rezultatą.

from math import sqrt as sq
print(sq(625))
print('.......')



# Visko importavimas iš modulio (nerekomenduojamas būdas)
# Užduotis 6:
# 1. Sukurkite Python programą, kuri naudoja from math import *.
# 2. Apskaičiuoja sinusą iš 90 laipsnių (naudojant sin()).
# 3. Išspausdina rezultatą.
# 4. Parašykite komentaruose, kodėl šis metodas gali būti pavojingas dideliuose
# projektuose.

from math import *
print('Sinusas is 90 laipsniu yra: ', sin(90))



# importuosim funkcijas is kito failo esancio toje pacioje papkeje

import aritmetikosmodulis as am

res = am.dalink(9, 3)
print(res)

res = am.daugink(5, 4)
print(res)

res = am.atimk(5, 6)
print(res)

res = am.sudek(10, 20)
print(res)

print('............')


# Importai iš mūsų sukurto modulio
#
# Užduotis 7:
# 1. Sukurkite naują Python failą aritmetikosmodulis.py.
# 2. Šiame faile parašykite funkcijas:
# a. sudetis(x, y), kuri grąžina dviejų skaičių sumą.
# b. daugyba(x, y), kuri grąžina dviejų skaičių sandaugą.
# 3. Sukurkite kitą Python failą main.py, kuris importuoja šias funkcijas ir jas iškviečia

from aritmetikosmodulis import  sudek, daugink
print(sudek(5, 10))
print(daugink(5, 10))
print('..............')


# Visas modulio importavimas
# Užduotis 8:
# 1. Sukurkite Python programą, kuri importuoja matematika modulį (sukurtą
# ankstesnėje užduotyje).
# 2. Naudoja matematika.sudetis(10, 20) ir matematika.daugyba(5, 4).
# 3. Išspausdina rezultatus.

import aritmetikosmodulis
print(aritmetikosmodulis.sudek(10, 20))
print(aritmetikosmodulis.daugink(5, 4))
print('..............')


# Specifinių funkcijų importavimas
# Užduotis 9:
# 1. Naudodami from matematika import sudetis, daugyba, importuokite tik tas
# funkcijas, kurios reikalingos.
# 2. Paskaičiuokite sumą ir sandaugą skaičių 8 ir 3.
# 3. Išspausdinkite rezultatus

from aritmetikosmodulis import sudek, daugink
print(f'Skaičių 8 ir 3 suma yra: {sudek(8, 3)},  sandauga: {daugink(8, 3)}')
print('.................')



# Modulio trumpinimas naudojant alias
# Užduotis 10:
# 1. Importuokite aritmetikosmodulis modulį kaip md.
# 2. Naudokite md.atimk(18, 10) ir md.dalink(72, 6).
# 3. Išspausdinkite rezultatus.

import aritmetikosmodulis as md
print(f'is skaičiaus 18 atemus 10 bus: {md.atimk(18, 10)},  72 padalinus is 6 bus: {md.dalink(72, 6)}')
