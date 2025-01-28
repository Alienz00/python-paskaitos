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