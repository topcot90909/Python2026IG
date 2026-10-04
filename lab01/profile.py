surname = input("Введите фамилию: ")
name = input("Введите имя: ")
group = input("Введите группу: ")
sity = input("Введите город: ")
age = int(input("Введите возраст: "))
if age < 1:
    print("Ошибка: возраст должен быть от 1 до 120.")
elif age > 120:
    print("Ошибка: возраст должен быть от 1 до 120.")
hours = float(input("Введите количество часов подготовки в неделю: "))
if hours < 0:
    print("Число не должно быть отрицательным")
item = input("Введите любимый предмет: ")

fullname = f"{name} {surname}"
age2 = age + 4
hours2 = hours * 4
day = hours / 7

print("-" * 25)
print("Карточка")
print("-" * 25)
print(f"Полное имя: {fullname}")
print(f"Возраст через 4 года: {age2}")
print(f"Время подготовки за 4 недели: {hours2:.2f}")
print(f"Среднее время подготовки в день: {day:.2f}")
