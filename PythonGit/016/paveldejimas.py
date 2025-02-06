# darom paprastai
class Kate:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f'{self.vardas} bega')

    def miauksi(self):
        print(f'{self.vardas} sako Miau')

cat = Kate('Murkis', 'Geltonas')
cat.begti()
cat.miauksi()
print('...........')


# cia su paveldejimu

class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f'{self.vardas} bega')

class Kate(Gyvunas):
    def miauksi(self):
        print(f'{self.vardas} sako Miau')

class Suo(Gyvunas):
    def loti(self):
        print(f'{self.vardas} loja')

cat = Kate('Murkis', 'Geltonas')
cat.begti()

dog = Suo('Margis', 'Margas')
dog.begti()
dog.loti()
print('..............')

# Paveldėjimas (Inheritance)
# Užduotis:
# Sukurkite bazinę klasę Gyvunas, kuri turi atributus vardas ir amzius.
# Pridėkite metodą judeti(), kuris spausdina, kad gyvūnas juda.
# Sukurkite dvi paveldinčias klases: Kate ir Suo.
# Kate klasėje pridėkite metodą miaukseti(), kuris sako "Vardas sako MIAU!"
# Suo klasėje pridėkite metodą lot(), kuris sako "Vardas sako AU AU!"
# Papildoma užduotis:
# Sukurkite Kate ir Suo objektus, iškvieskite jų metodus ir patikrinkite, ar paveldėjimas
# veikia.

class Gyvunas:

    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def judeti(self):
        print(f'{self.vardas} judada')

    def amzius(self):
        print(f'{self.vardas} yra {self.amzius} metu amziaus')

class Suo(Gyvunas):
    def loti(self):
        print(f'{self.vardas} loja')

class Kate(Gyvunas):
    def miaukti(self):
        print(f'{self.vardas} uzknisa')

dog = Suo('Bosis', '12')
dog.loti()
dog.amzius()

cat = Kate('Murka', 5)
cat.judeti()
cat.miaukti()