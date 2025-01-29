
def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs['pirmas'])
    print(type(kwargs))

print_kwargs(pirmas=3, antras=2)


def print_list(listas, skirtukas=' ', eilutes_pabaiga='\n'):
    for elem in listas:
        print(elem, 'men.', sep=skirtukas, end=eilutes_pabaiga)

listas_duom = ['sausio', 'vasario', 'kovo']
print_list(listas_duom)
print('..................')
print_list(listas_duom, skirtukas='|||', eilutes_pabaiga='***\n')


# o cia naudojant kwargs

def print_lyst(listas, **kwargs):
    for elem in listas:
        print(elem, 'men', **kwargs)
listas_duom = ['sausio', 'vasario', 'kovo']
print_lyst(listas_duom, sep='>>>', end='<<<\n')


# Įvadas į **kwargs
#
# Užduotis 7:
# Parašykite funkciją rodyti_duomenis(**kwargs), kuri išspausdintų visus perduotus
# vardinius argumentus raktu ir reikšme.

def muzika(stiliai, **kwargs):
    for stilius in stiliai:
        print(stilius, 'muzika', **kwargs)
stiliu_sarasas = ['Techno', 'Jungle', 'Psychedelic trance']
muzika(f'>>>, {stiliu_sarasas}, end=<<<\n') #kodel taip printina?