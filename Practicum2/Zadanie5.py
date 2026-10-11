a,b,c = map(int, input().split())
if a >= b:
    m = a
    if c >= a:
        m = c
    print(m)
else:
    m = b
    if c >= b:
        m = c
    print(m)