s = input()
col1_letter = s[0]
row1 = int(s[1])
col2_letter = s[3]
row2 = int(s[4])
if col1_letter == 'a':
    col1 = 1
elif col1_letter == 'b':
    col1 = 2
elif col1_letter == 'c':
    col1 = 3
elif col1_letter == 'd':
    col1 = 4
elif col1_letter == 'e':
    col1 = 5
elif col1_letter == 'f':
    col1 = 6
elif col1_letter == 'g':
    col1 = 7
else:
    col1 = 8
if col2_letter == 'a':
    col2 = 1
elif col2_letter == 'b':
    col2 = 2
elif col2_letter == 'c':
    col2 = 3
elif col2_letter == 'd':
    col2 = 4
elif col2_letter == 'e':
    col2 = 5
elif col2_letter == 'f':
    col2 = 6
elif col2_letter == 'g':
    col2 = 7
else:
    col2 = 8
dx = col1 - col2
if dx < 0:
    dx = -dx
dy = row1 - row2
if dy < 0:
    dy = -dy
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("верно")
else:
    print("ошибка")