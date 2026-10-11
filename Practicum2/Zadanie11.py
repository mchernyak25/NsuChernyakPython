from math import *
xcent = int(input())
ycent = int(input())
r = int(input())
x = int(input())
y = int(input())
dist_oc_toch = sqrt((x - xcent) ** 2 + (y - ycent) ** 2)

if dist_oc_toch == r:
    print("на окружности")
elif dist_oc_toch < r:
    print("внутри окружности")
else:
    print("вне окружности")