# Sukurkite funkciją sveikink(), kuri tris kartus iš eilės atspausdintų pasisveikinimą:
# „Labas!“. Iškvieskite šią funkciją programoje.

def sveikink():
    for _ in range(3):
        print('Liabuka :*')
sveikink()

print('....................')
sveikink()



def say_bye():
    ...  # tokia funkcija nieko nedaro
    say_bye()

print('.................')


def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
    if not iki_sveiko_sk:
        return sk1/sk2
    return sk1 // sk2

print(
    dalink_spec(777, 5, True)
)



def modify_product(product, inform_client=False):
    if inform_client:
        print('produkta modifikavo sistema')
    return product * 50

print(modify_product('Tapkes, True. '))
print(modify_product('Trusikai, '))
print('......................')


# doc stringai

def say_hello(name):
    """
    Ši funkcija priima vieną argumentą 'name' ir atspausdina pasveikinimą.
    """
    print(f'Hello, {name}!')

# Iškviesti funkciją su argumentu 'Vytautas'
say_hello('Vytautas')

# Atspausdinti docstring'ą
print(say_hello.__doc__)

print('....Nauja tema: Type funkc....')


def add(x: int, y: int) -> int:
    return x + y
a = 1 + add(1, 9)
print(a)

print('...............')


# Loginiai jungikliai funkcijose

# Užduotis 5:
# Sukurkite funkciją skaiciuoti_sumos_tipą(x, y, tik_teigiama=False), kuri
# priimtų du skaičius ir grąžintų jų sumą.
# • Jei tik_teigiama=True, funkcija grąžintų tik teigiamą sumą (jei suma neigiama,
# grąžintų 0).

def skaiciuoti_sumos_tipą(x, y, tik_teigiama=False) -> int:
    suma = x + y
    if tik_teigiama:
        return suma if suma > 0 else 0
    return suma

print(skaiciuoti_sumos_tipą(88, 44, tik_teigiama=True))
print(skaiciuoti_sumos_tipą(-88, 44, tik_teigiama=True))
print(skaiciuoti_sumos_tipą(-88, -44, tik_teigiama=True))
print(skaiciuoti_sumos_tipą(88, -44, tik_teigiama=True))

print('.............')
# destytojo

def skaiciuoti_sumos_tipą(x, y, tik_teigiama=False) -> int:
    suma = x + y
    if tik_teigiama:
        return max(suma, 0)
    return suma
print(skaiciuoti_sumos_tipą(88, 44, tik_teigiama=True))
print(skaiciuoti_sumos_tipą(-88, 44, tik_teigiama=True))
print(skaiciuoti_sumos_tipą(-88, -44, tik_teigiama=True))
print(skaiciuoti_sumos_tipą(88, -44, tik_teigiama=True))
print('.........................')



# Užduotis 6:
# Sukurkite funkciją apskaiciuok_vidurki(skaiciai), kuri apskaičiuotų ir grąžintų
# sąrašo skaičių vidurkį. Pridėkite docstring su informacija apie:
# • Funkcijos paskirtį.
# • Argumentus (sąrašas skaičių).
# • Grąžinamą reikšmę (vidurkis)

skaiciai = [11, 88, 66, 77, 22, 33, 44, 55, 99]
def apskaiciuokite_vidurki(skaiciai):
    """
    Apskaičiuoja ir grąžina sąrašo skaičių vidurkį.

    Argumentai:
    skaiciai (list): Sąrašas skaičių.

    Grąžinama reikšmė:
    float: Skaičių vidurkis.
    """
    vidurkis = sum(skaiciai) / len(skaiciai)
    return vidurkis
print(apskaiciuokite_vidurki(skaiciai))

print(',,,.....oo.....,,,')

# Type hints ir anotacijos
# Užduotis 7:
# Sukurkite funkciją prideti_zodi(tekstas: str, zodis: str) -> str, kuri priimtų
# sakinį ir pridedamą žodį, o tada grąžintų sakinį su tuo žodžiu gale.

def prideti_zodi(tekstas: str, zodis: str) -> str:
    """
       Priima sakinį ir pridedamą žodį, o tada grąžina sakinį su tuo žodžiu gale.

       Argumentai:
       tekstas (str): Pradinis sakinys.
       zodis (str): Žodis, kurį reikia pridėti.

       Grąžinama reikšmė:
       str: Sakinys su pridėtu žodžiu gale.
       """
    if not tekstas or not zodis:
        return
    sakinys = tekstas + " " + zodis
    return sakinys
print(prideti_zodi('Lietus lyja, sakos braska, man nesalta su: ', 'rubaske'))