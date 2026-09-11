from random import randint

names = ['Mari', 'Anna', 'Villem', 'Jüri'] # List

# Väljasta listis olevad nimed nime kaupa.
for name in names:
    print(name) # Väljasta nimi

print() # Tühi rida

# Sama lahendus nagu enne, aga lisaks juhuslik vanus
for x in range(len(names)):
    print(x, names[x], randint(1, 122))

print()

for x in range(1, 5): # 1 2 3 4
    print(x, end=' ') # Ei tee reavahetust
print('\n') # Reavahetus + tühi rida

for x in range(0, 10, 2): # 0 | 2 | 4 | 6 | 8 |
    print(x, end=' | ')
print('\n') # Reavahetus + tühi rida

# while-loop
x = 0
while x < len(names):
    print(names[x])
    x += 1 # x = x + 1

# ÜLESANNE: Väljasta listi nimed konsooli ja iga nime ette 
# pane järjekorra number koos punktiga. Seega:
# 1. Mari
# 2. Anna
# ....

# Lahendus 1:
for x in range(len(names)):
    print(f'{x+1}. {names[x]}')

print()

# Lahendus 2:
x = 0
while x < len(names):
    print(str(x+1) + '. ' + names[x])
    x += 1