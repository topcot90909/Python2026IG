a = int(input("Введите целое число :"))
b = int(input("Введите целое число :"))

step = 1 if a < b else -1
current = a
while True:
    print(current)
    if current == b:
        break
    current += step
b = int(input())