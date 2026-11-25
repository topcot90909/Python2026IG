a = int(input("ВВедите колличесво чисел :"))
summ = 0
count_positive = 0
maximum = None

for i in range(a):
    num = int(input("Введите число :"))
    
    summ += num
    
    if num > 0:
        count_positive += 1
        
    if maximum is None:
        maximum = num
    elif num > maximum:
        maximum = num

print(summ)
print(count_positive)
print(maximum)