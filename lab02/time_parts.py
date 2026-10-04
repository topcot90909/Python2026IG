total_seconds = int(input("Введите количество секунд: "))

hours = total_seconds // 3600
hours2 = total_seconds % 3600
minuts = hours2 // 60
sec = hours2 % 60

print(f"{hours} ч {minuts} мин {sec} с")