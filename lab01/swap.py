first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("Исходные значения:")
print(f"первая аудитория: {first_room}")
print(f"вторая аудитория: {second_room}")

arbuz = first_room
first_room = second_room
second_room = arbuz

print("\nПосле обмена:")
print(f"первая аудитория: {first_room}")
print(f"вторая аудитория: {second_room}")