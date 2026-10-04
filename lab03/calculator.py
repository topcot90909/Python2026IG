a = float(input("Введите первое число: "))
op = input("Введите операцию: ")
b = float(input("Введите второе число: "))

if op == "+":
    res = a + b
    print(f"Результат: {res:.2f}")
elif op == "-":
    res = a - b
    print(f"Результат: {res:.2f}")
elif op == "*":
    res = a * b
    print(f"Результат: {res:.2f}")
elif op == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        res = a / b
        print(f"Результат: {res:.2f}")
else:
    print("Неизвестная операция")