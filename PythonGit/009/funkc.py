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

x = 5
y = 10

def sudaugink(x, y):
    daugyba = x * y
    return daugyba

rezultatas = sudaugink(x, y)
print(rezultatas)