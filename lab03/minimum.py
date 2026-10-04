a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a <= b and a <= c:
    mini = a
elif b <= a and b <= c:
    mini = b
else:
    mini = c

print(f"Минимальное число: {mini}")