order = input("Введите название заказа: ")
customer = input("Введите имя заказчика: ")

name1 = input("Введите название первой позиции: ")
count1 = int(input(f"Введите количество: "))
price1 = float(input(f"Введите цену за единицу в рублях: "))

name2 = input("Введите название второй позиции: ")
count2 = int(input(f"Введите количество: "))
price2 = float(input(f"Введите цену за единицу в рублях: "))

deliver = float(input("Введите стоимость доставки в рублях: "))
pay = float(input("Введите внесённую сумму в рублях: "))

fullprice1 = count1 * price1
fullprice2 = count2 * price2
price3 = fullprice1 + fullprice2
fullpay = price3 + deliver
countfull = count1 + count2
change = pay - fullpay

print("-" * 25)
print("Заказ:", order)
print("Заказчик:", customer)
print("-" * 25)
print(f"{name1} | {count1} | {price1:.2f} | {fullprice1:.2f}")
print(f"{name2} | {count2} | {price2:.2f} | {fullprice2:.2f}")
print("-" * 25)
print(f"Стоимость товаров без доставки: {price3:.2f} руб.")
print(f"Общая сумма с доставкой: {fullpay:.2f} руб.")
print(f"Общее количество единиц: {countfull}")
print(f"Сдача: {change:.2f} руб.")
print("-" * 25)