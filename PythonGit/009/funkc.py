name = 'Vytautas'

def create_greetings(user):
    res = f'Greetings, {user}'
    return res

print(
    create_greetings(name)
)




name = ''
def create_greetings(user):
    if not user:
        return
    res = f'Greetings, {user}'
    return res

greetings = create_greetings(name)
if greetings:
    print(greetings)
else:
    print('User not found')

# Argumentai ir return reikšmės
# Užduotis 2:
# Sukurkite funkciją sudaugink(x, y), kuri priimtų du skaičius ir
# grąžintų jų sandaugą.
# 1. Iškvieskite funkciją su reikšmėmis 5 ir 10.
# 2. Išspausdinkite grąžintą rezultatą.



def sudaugink(x, y):
    daugyba = x * y
    return daugyba

rezultatas = sudaugink(5, 10)
print(rezultatas)
print('................')

# destytojo

def daugink(x, y):
    if not x or not y:
        return
    return x * y

suma = daugink(5, 10)
if suma:
    print(suma)
else:
    print('Netinkami skaiciai')

# pasveikins 2
def say_hi_to_two(name1, name2):
    if not name1 or not name2:
        return
    hello_string = f'Hello to {name1} and hello to {name2}'
    return hello_string
pasveikinimas = say_hi_to_two('Petras', 'Kazys')
print(pasveikinimas)


# ives teksta sutrumpintai
def greet(name='Jimm'):
    print(f'Hello, {name}!')

greet('Vytautas')
greet()


# argumentai, kuriems butinai reikia perduoti reiksme

def priimk_pacienta(ligonis, gydytojas='gyd. Pagalnutylenis'):
    irasas_gyd_zurnale = f'Pacientas {ligonis}, prieme {gydytojas}'
    return irasas_gyd_zurnale

res = priimk_pacienta('Adomas')
print(res)
print('...........')

res = priimk_pacienta('Kazys')
print(res)
print('...........')

res = priimk_pacienta('Petras', 'gyd. Pakaitenis')
print(res)
print('...........')


# Sukurkite funkciją trys_sveikinimai(vardas1, vardas2, vardas3),
# kuri priimtų tris
# vardus ir kiekvienam iš jų atspausdintų pasisveikinimą.
# Pvz.: „Labas, Jonas!“, „Labas, Asta!“, „Labas, Mantas!“

def trys_pasveikinimai(vardas1, vardas2, vardas3):
    if not vardas1 or not vardas2 or not vardas3:
        return
    sveikinu = f'Labas, {vardas1}, Labas {vardas2} ir labas {vardas3}'
    return sveikinu

pasisveikink = trys_pasveikinimai('Jonas', 'Asta', 'Mantas')
print(pasisveikink)


# Numatytosios reikšmės ir keyword argumentai
# Užduotis 4:
# Sukurkite funkciją sveikink_su_pavadinimu(vardas, pavadinimas="drauge"), kuri
# atspausdintų žinutę: „Sveikas, [vardas]! Ką veiki, [pavadinimas]?“.
# 1. Iškvieskite funkciją nenurodydami pavadinimo.
# 2. Iškvieskite funkciją, nurodydami pavadinimą „kolega“.

pavadinimas = 'drauge'
def sveikink_su_pavadinimu(vardas, pavadinimas):
    if not vardas or not pavadinimas:
        return
    zinute = f'Sveikas, {vardas}! Ka veiki, {pavadinimas}'
    return zinute

be_pav = sveikink_su_pavadinimu('Petras', pavadinimas)
print(be_pav)

su_pav = sveikink_su_pavadinimu('Kazys', 'Kolega')
print(su_pav)

