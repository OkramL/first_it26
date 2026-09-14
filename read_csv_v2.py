# read_csv_v2.py

"""
TÄIENDUS: Loenda kokku mitu numbrit kokku liidetakse.
Näita ka vastust.
"""

filename = 'Create-MyCSV-v.csv'
total = 0 # Kogu veeru summa
count = 0 # Numbrite loendamiseks (TÄIENDUS)

# Loe kokku mitu veergu on failis
f = open(filename, 'r') # Ava fail lugemiseks
rows = len(f.readline().split(';')) # Mitu elementi reas
f.close() # Sulge fail

row = int(input(f'Mimtes veerg kokku liita? 1-{rows} '))

if row >= 1 and row <= rows:
    row -= 1 # row = row - 1    
    with open(filename, 'r') as f:
        content = f.readlines()
        for line in content:
            line = line.strip() # Korrasta rida (eemalda \n)
            parts = line.split(';')
            if parts[row].isnumeric():
                total += int(parts[row])
                count += 1 # kasvab ühe võrra
                
        print(total, count)

else:    
    print('Vigane veeru number!')

