price = int(input("Введите цену одной тетради в рублях: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму в рублях: "))

fullprice = price * count
change = paid - fullprice

print(f"Стоимость: {fullprice}")
print(f"Сдача: {change}")

a = input("")