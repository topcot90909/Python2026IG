total = int(input("Введите количество студентов: "))
capacity = int(input("Введите количество мест в автобусе: "))

full = total // capacity
free = total % capacity
mini = (total + capacity - 1) // capacity

print(f"Полностью заполненных автобусов: {full}")
print(f"Остаток студентов: {free}")
print(f"Минимальное число автобусов: {mini}")