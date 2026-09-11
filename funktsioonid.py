# funktsioonid.py
def welcome():
    print('Tere, kuidas läheb?')


def welcome_name(name):
    return f'Tere, {name}!'


def divison(number1, number2):
    """Teostab kahe arvu jagamist"""
    if number2 != 0:
        return number1 / number2
    return -1 # See on viga ehk 0 jagamine


def introduce(name, age=20):
    """
    Loob lihtsa tutvustava lause

    :param name: str Isiku nimi
    :param age: int Isiku vanus (vaikimisi 20)
    :return: Tekstiline tutvustav lause
    :rtype: string
    """
    return f'Tema on {name} ja ta on {age} aastane!'


welcome()
for x in range(3):
    welcome()

print() # Tühi rida

print(welcome_name('Marko'))
names = ['Juhan', 'Mari', 'Margus']
for nimi in names:
    print(welcome_name(nimi))
print(welcome_name(1234)) # Tere, 1234!
print(welcome_name('')) # Tere, !
print() # Tühi rida

print(divison(4, 2))
print(divison(10, 0))
print()

print(introduce('Marko', 25))
print(introduce('Juhan'))
print(introduce(''))
print(introduce(1234, 56))
print(introduce(age=99, name='Vanaema'))

print(divison(number2=10, number1=100))
