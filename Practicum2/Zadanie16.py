a = int(input())
if a % 10 != (a//1000) != (a%100)//10 != (a%1000)//100:
    if len(str(a)) == 4:
        if a > 2050 or a < 1900:
            print("OK")
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")