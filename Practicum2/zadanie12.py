a = int(input())
if a % 10 == 1:
    print(str(a), "попугай")
elif (a % 10 == 2 or a % 10 == 3 or a % 10 == 4) and a != 12 and a != 13 and a != 14:
    print(str(a), "попугая")
elif 5 <= a%10 <= 9 or a % 10 == 0 or a == 11 or a == 12 or a == 13 or a == 14:
    print(str(a), "попугаев")