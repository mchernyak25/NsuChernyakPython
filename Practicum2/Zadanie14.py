kn = int(input())
s = kn // 29
kn = kn - s * 29
g = s // 17
s = s - g * 17
if g != 0:
    print(str(g), "галлеонов")
if s != 0:
    print(str(s), "сиклей")
if kn != 0:
    print(str(kn), "кнатов")
