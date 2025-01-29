# Kelių argumentų tipų derinimas
# Užduotis 5:
# Sukurkite funkciją spausdinti_zinutes(kartai, *args, pabaiga="!"), kuri
# pakartotų kiekvieną perduotą žinutę kartai kartų, o pabaigoje pridėtų pabaiga reikšmę
# sunumeruotu is eiles

def spausdinti_zinutes(kartai, *args, pabaiga="!"):
    for zinute in args:
        for i in range(1, kartai + 1):
            print(f'{i}. Idomi zinute: {zinute}{pabaiga}')

spausdinti_zinutes(7, 'Maklimakakinam',)
print('..................')


# Rezultatų grąžinimas naudojant *args
# Užduotis 6:
# Sukurkite funkciją dauginti_skaicius(n, *args), kuri priimtų skaičių n ir kitus
# skaičius *args, padaugintų kiekvieną iš n, o rezultatą grąžintų kaip sąrašą.

def dauginti_skaicius(n, *args):
    sudauginti = [elem * n for elem in args]
    return sudauginti

res = dauginti_skaicius(15, 8, 5, 6, 9, 85)
print(res)