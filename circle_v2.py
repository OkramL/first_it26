from math import pi, pow

def perimeter(r):
    return 2 * pi * radius

def area(r):
    return pi * pow(r, 2)

radius = float(input('Sisesta ringi raadius: '))

if radius < 1 or radius > 10:
    print('Raadius vales vahemikus.')
else:    
    print(f'Raadius: {radius}')
    print(f'Ümbermõõt: {perimeter(radius)}')
    print(f'Pindala: {area(radius)}')
