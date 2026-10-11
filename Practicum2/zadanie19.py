a, b = map(int, input().split("x"))
k = int(input())
if k < a * b and (k % a == 0 or k % b == 0):
    print("Успешно")
else:
    print("Неосуществимо")