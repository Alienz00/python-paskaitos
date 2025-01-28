import random

atsitiktinis_skaicius = random.randint(1, 10)

print(f'Atisitktinis int skaicius nuo 1 iki 10 :{atsitiktinis_skaicius}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{atsitiktinis_skaicius}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{atsitiktinis_skaicius}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{atsitiktinis_skaicius}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{atsitiktinis_skaicius}')
print('...........skirsis, nes nurodyta kiekvienam print vel skaiciai......')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{random.randint(1, 10)}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{random.randint(1, 10)}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{random.randint(1, 10)}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{random.randint(1, 10)}')
print(f'Atisitktinis int skaicius nuo 1 iki 10 :{random.randint(1, 10)}')
print('.......................................................')


# Paprastas importavimas

# Užduotis 2:
# Sukurkite Python programą, kuri importuoja random modulį ir:
# 1. Sugeneruoja atsitiktinį skaičių nuo 1 iki 100.
# 2. Sugeneruoja atsitiktinį skaičių su uniform(), kuris yra tarp 1 ir 50.
# 3. Išspausdina abu rezultatus.

import random
randomas = random.randint(1, 100)
print(f'Atsitiktinis sk nuo 1 iki 100 yra: {randomas}')
print('.......................................................')

uniforminis = random.uniform(1, 50,)
print(f'uniforminis skaicius yra: {uniforminis}')
print('.......................................................')

# sutrumpintai
print(random.randint(200, 500))
print(round(random.uniform(5000, 10000), 5))
print('.............')



from random import randint # importuos tik sias dvi funkcijas

random_number = randint(1, 10)
print(random_number)



random_month = random.choice(['sausis', 'vasaris', 'kovas'])
print(random_month)

print('.............')


# galima random pervedinti i sutrumpinima

import random as rn
rand_nr = rn.randint(5, 7)
print(rand_nr)
print('............')


# 3. Specifinių funkcijų importavimas
# Užduotis 3:
# Sukurkite Python programą, kuri naudoja:
# 1. from random import randint, choice
# 2. Sugeneruoja atsitiktinį skaičių nuo 1 iki 10 naudojant randint().
# 3. Pasirenka atsitiktinį elementą iš sąrašo ['obuolys', 'bananas', 'kriaušė', 'vyšnia'] naudodama choice().
# 4. Išspausdina abu rezultatus.

from random import randint, choice
print(randint( 1, 10))

print(choice(['obuolys', 'bananas', 'kriaušė', 'vyšnia']))
print('...............')


# 4. Modulio trumpinimas naudojant alias
# Užduotis 4:
# Sukurkite Python programą, kuri:
# 1. Importuoja datetime modulį su alias dt.
# 2. Naudoja dt.datetime.now() funkciją, kad gautų dabartinę datą ir laiką.
# 3. Išspausdina rezultatą su formatu: Dabartinė data ir laikas: YYYY-MM-DD
# HH:MM:SS.

import datetime as dt
dabartine = dt.datetime.now()
print(dabartine)

suapvalinta = dabartine.replace(microsecond=0)
print(suapvalinta)
print('...............')

print('Dabar yra: ', dt.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
print('............')

# allias sutrumpinimai

from random import randint as rnt
print(rnt(10, 20))

# tokio b8do nenaudoti
from random import *
parinktis = sample(['sausis', 'vasaris', 'kovas'], k=3)
print(parinktis)


