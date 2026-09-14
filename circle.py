from math import pi, pow

radius = float(input('Sisesta ringi raadius: '))

if radius < 1 or radius > 10:
    print('Raadius vales vahemikus.')
else:
    P = 2 * pi * radius # Ümbermõõt
    A = pi * pow(radius, 2) # Pindala
    print(f'Raadius: {radius}')
    print(f'Ümbermõõt: {P}')
    print(f'Pindala: {A}')
