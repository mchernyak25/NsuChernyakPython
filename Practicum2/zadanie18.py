a,b = map(int, input().split('x'))
c,d,e = map(int, input().split('x'))
otv1 = a * b
if c >= d and c >= e:
    otv = d * e
elif d >= c and d >= e:
    otv = c * e
elif e >= c and e >= d:
    otv = c * d
if otv1 >= otv:
    print("да")
else:
    print("нет")