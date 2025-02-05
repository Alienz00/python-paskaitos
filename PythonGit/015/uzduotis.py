# Galutinė Užduotis: Knygų Bibliotekos Sistema
# Šioje užduotyje naudosime viską, ką išmokome šiame pokalbyje: klases, metodus, sąrašų
# valdymą, paveldimumą, datetime modulį, try-except, *args, **kwargs, ir dar daugiau.
# Užduotis: Sukurkite paprastą bibliotekos valdymo
# sistemą
# 1. Reikalavimai:
# • Sukurti dvi klases: Book ir Library.
# • Naudoti datetime modulį knygų paskolos laikotarpiams valdyti.
# • Naudoti *args ir **kwargs knygų filtravimui.
# • Naudoti try-except klaidų valdymui.
# 2. Žingsniai:
# ŽINGSNIS 1: Sukurkite klasę Book
# • Laukai:
# o title (pavadinimas)
# o author (autorius)
# o year (išleidimo metai)
# o available (ar knyga prieinama) – pagal nutylėjimą True
# • Metodai:
# o __str__ – grąžina informaciją apie knygą gražiu formatu.
# o is_classic() – grąžina True, jei knyga išleista daugiau nei prieš 50 metų.
# ŽINGSNIS 2: Sukurkite klasę Library
# • Laukai:
# o books (sąrašas, kuriame saugomos knygos)
# • Metodai:
# o add_book(book) – prideda naują Book objektą į biblioteką.
# o display_books() – atvaizduoja visas knygas bibliotekoje.
# o borrow_book(title) – leidžia pasiskolinti knygą, jei ji prieinama.
# ▪ Naudoti try-except, kad suvaldytumėte klaidas (pvz., jei knygos
# nėra).
# o return_book(title) – leidžia grąžinti knygą.
# o filter_books(*args, **kwargs) – leidžia filtruoti knygas pagal autorių,
# metus ar pavadinimą.
# ▪ Pvz.: filter_books(author="Jonas") arba
# filter_books(year=2000)
# ŽINGSNIS 3: Naudokite datetime paskolos valdymui
# • Kai vartotojas pasiskolina knygą, įrašykite paskolos datą.
# • Pridėkite metodą due_date(), kuris grąžins datą, kada knyga turi būti grąžinta
# (pvz., po 14 dienų).
# ŽINGSNIS 4: Sukurkite sąveiką su vartotoju
# • Naudokite while ciklą, kad vartotojas galėtų:
# o Pridėti naują knygą į biblioteką.
# o Peržiūrėti visą bibliotekos knygų sąrašą.
# o Pasiskolinti knygą.
# o Grąžinti knygą.
# o Filtruoti knygas pagal autorių, metus ar pavadinimą.
# o Išeiti iš programos.
# 3. Papildomos Sąlygos:
# • Naudokite try-except klaidoms suvaldyti, pvz., neteisingai įvedus metus.
# • Naudokite *args ir **kwargs knygų filtravimui pagal skirtingus kriterijus.

import datetime
import keyboard


class Book:
    def __init__(self, author, title, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.due_date = None

    def __str__(self):
        status = ' (Klasikinė)' if self.is_classic() else ''
        availability = ' (Pasiskolinta)' if not self.available else ''
        due_date_str = f' Grąžinimo data: {self.due_date}' if self.due_date else ''
        return f'Autorius: {self.author}. Pavadinimas: {self.title}. Išleidimo metai: {self.year}{status}{availability}{due_date_str}'

    def is_classic(self):
        return datetime.datetime.today().year - self.year > 50

    def borrow(self):
        if self.available:
            self.available = False
            self.due_date = datetime.datetime.today() + datetime.timedelta(days=14)
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            return True
        return False

books = [
    Book('Delia Owens', 'Ten, kur gieda vėžiai', 2018),
    Book('Hanya Yanagihara', 'Mažas gyvenimas', 2015),
    Book('Kristina Sabaliauskaitė', 'Petro imperatorė II', 2020),
    Book('Matt Haig', 'Vidurnakčio biblioteka', 2020),
    Book('Norbertas Černiauskas', '1940. Paskutinė Lietuvos vasara', 2020),
    Book('Kazuo Ishiguro', 'Klara ir saulė', 2021),
    Book('Claire Lombardo', 'Mūsų smagiausios dienos', 2019),
    Book('Brene Brown', 'Didi drąsa', 2012),
    Book('Harper Lee', 'Nežudyk strazdo giesmininko', 1960),
    Book('Pilar Quintana', 'Kalė', 2023),
    Book('Vaiva Rykštaitė', 'Mėlynas namas Havajuose', 2022),
    Book('Virginija Kulvinskaitė', 'Keturi', 2023),
    Book('Donato Carrisi', 'Blogio šnabždesys', 2017),
    Book('Peter Frankopan', 'Šilko kelias', 2015),
    Book('Yuval Noah Harari', 'Sapiens: Glausta žmonijos istorija', 2011),
    Book('Margaret Atwood', 'Tarnaitės pasakojimas', 1985),
    Book('Paulo Coelho', 'Alchemikas', 1988),
    Book('F. Scott Fitzgerald', 'Didysis Getsbis', 1925),
    Book('George Orwell', '1984-ieji', 1949),
    Book('J.R.R. Tolkien', 'Žiedų valdovas', 1954)
]

Library = books.copy()

def prideti():
    author = input('Iveskite autorių: ')
    title = input('Iveskite pavadinimą: ')
    year = int(input('Iveskite išleidimo metus: '))

    nauja_knyga = Book(author, title, year)
    Library.append(nauja_knyga)

    for book in Library:
        print(book)

def view_books():
    print('Bibliotekos knygos:')
    for book in Library:
        print(book)


def grazinimo_data():
    dabar = datetime.datetime.today()
    dvi_savaites = datetime.timedelta(days=14)
    grazinti = dabar + dvi_savaites

def pasiskolinti():
    title = input('Iveskite knygos pavadinimą, kurią norite pasiskolinti: ')
    for book in Library:
        if book.title == title:
            if book.borrow():
                print(f'Jūs pasiskolinote knygą: {book.title} iki {book.due_date}')
            else:
                print(f'Knyga {book.title} jau paskolinta')
            return
    print(f'Knyga {title} nerasta')

def grazinti():
    title = input('Iveskite knygos pavadinimą, kurią norite grąžinti: ')
    for book in Library:
        if book.title == title:
            if book.return_book():
                print(f'Jūs grąžinote knygą: {book.title}')
            else:
                print(f'Knyga "{book.title}" nebuvo pasiskolinta.')
            return
    print(f'Knyga "{title}" nerasta.')

def ieskoti():
    search_term = input('Iveskite paieškos terminą (autorius arba pavadinimas): ')
    found_books = [book for book in Library if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
    if found_books:
        print('Rastos knygos:')
        for book in found_books:
            print(book)
    else:
        print('Knygų nerasta.')

def main_meniu():
    print('1. Pridėkite naują knygą')
    print('2. Peržiūrėti bibliotekos knygas')
    print('3. Pasiskolinti knygą')
    print('4. Grąžinti knygą')
    print('5. Filtruoti knygas')
    print('6. Išeiti')

while True:
    main_meniu()
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == '1':
            prideti()
        elif event.name == '2':
            view_books()
        elif event.name == '3':
            pasiskolinti()
        elif event.name == '4':
            grazinti()
        elif event.name == '5':
            ieskoti()
        elif event.name == '6':
            break

