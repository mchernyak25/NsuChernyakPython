r = 6.5
a,b = map(int, input().split("x"))
diagkv12 = (a**2+b**2)**0.5 / 2
if r >= diagkv12:
    print("да")
else:
    print("нет")