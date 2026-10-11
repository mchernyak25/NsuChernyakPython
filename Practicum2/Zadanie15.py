vsego, otk, kud = map(int, input().split())
a1 = vsego - otk - 1 + kud
a2 = abs(kud - otk) - 1
if a1 <= a2:
    print(a1)
else:
    print(a2)
