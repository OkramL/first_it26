# listid
# List ehk massiiv
# List [nimekiri, loend], tuple (järjend), dictionary {sõnastik}

places = [] # Loo tühi list
places.append('Kehtna') # Lisa uus koht listi lõppu
places.append('Rapla')
places[1:1] = ['Tallinn', 'Pärnu'] # Lisa Kehtna ja Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) # Lisa lõppu
places.insert(2, 'Are')

numbers = [1, 7, 4, 25, -32]

print(places) # Näita kohanimede listi
print(numbers) # Näita numbrite listi
print(type(places)) # näita kohanimede muutuja tüüpi

# Kustutamine
places.remove('Rapla') # Esimene eemdaldatakse
places.pop(6) # Viimane Rapla
del places[2] # Kustutab Are

# Ülesanne: Lisa Rapla, Pärnu ja Viljandi vahele ning listi lõppu
places.insert(3, 'Rapla')
places.append('Rapla')
print(places)

# Leiame elemendi indeksi ja mitu korda esineb (Rapla)
place = places[-1] # Nimekirja viimane Rapla
index = places.index(place) # Mis indeks on esimene Rapla
count = places.count(place) # Mitu Raplat leiti

print(place, index, count)

if place in places:
    print(f'{place} on nimekirjas olemas.')

if 'Kohila' in places:
    print(f'Kohila on nimekirjas olemas.') # Seda rida ei tule vastusesse

print(len(places)) # Listi suurus
print(places[len(places)-1]) # Viimane element listist (Rapla)

# Koopia listist
list_copy = places.copy()
list_list = list(places) # ?

# Sorteerimine
list_copy.sort() # A->Z
new_list_list = sorted(places, reverse=True) # Z->A

print(list_copy) # Sorteeritud A-Z
print(new_list_list) # Z-A
print(places) # Originaal

print() # Tühi rida

# Tühjenda list
new_list_list.clear()
print(new_list_list)

"""
Ülesanne: kasuta originaal listi ja eemalda listist viimane Rapla
ilma [-1] kasutamata. Väljasta kolmanda elemendi keskmine täht
SUURTÄHENA
"""
places.pop(len(places)-1) # Eemalda lisati viimane Rapla
print(places) # Kontrolli eelmise rea tulemust
print(places[2][2].title()) # Pärnu => R
