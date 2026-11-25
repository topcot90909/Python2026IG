attempts = 0

while True:
    a = int(input("Введите целое число :"))
    
    if a > 0:
        print(a ** 2)
        break
    else:
        attempts += 1

print(attempts)