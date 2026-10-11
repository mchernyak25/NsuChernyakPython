cell = input()

col = cell[0]
row = int(cell[1])

if col == 'a' or col == 'c' or col == 'e' or col == 'g':
    if row == 1 or row == 3 or row == 5 or row == 7:
        print("черный")
    else:
        print("белый")
else:
    if row == 1 or row == 3 or row == 5 or row == 7:
        print("белый")
    else:
        print("черный")