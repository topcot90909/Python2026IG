lesson1 = input("Первый предмет: ")
lesson2 = input("Второй предмет: ")
count1 = int(input("Введите количество занятий по первому предмету за неделю: "))
if count1 < 0:
    print("необходимо неотрицательное число")
count2 = int(input("Введите количество занятий по второму предмету за неделю: "))
if count2 < 0:
    print("необходимо неотрицательное число")
time1 = int(input("Введите продолжительность занятия по первому предмету в минутах: "))
if time1 < 1:
    print("необходимо положительное число")
time2 = int(input("Введите продолжительность занятия по второму предмету в минутах: "))
if time2 < 1:
    print("необходимо положительное число")
available = int(input("Введите доступное время на неделю в часах: "))
if available < 1:
    print("необходимо положительное число")

load1 = count1 * time1
load2 = count2 * time2
loadall = load1 + load2
loadall2 = loadall / 60
available2 = available - loadall2
loadall4 = loadall2 * 4

print("-" * 25)
print("Таблица нагрузки")
print("-" * 25)
print(f"Предмет {lesson1}: {load1} мин/неделю")
print(f"Предмет {lesson2}: {load2} мин/неделю")
print("-" * 25)
print(f"Общая нагрузка: {loadall} мин = {loadall2:.2f} ч")
print(f"Остаток свободного времени: {available2:.2f} ч")
print(f"Нагрузка за 4 недели: {loadall4} минут")