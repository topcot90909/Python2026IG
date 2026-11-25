data = input().split()
if not data:
    print("Нет данных")
else:
    numbers = [int(x) for x in data]
    count = len(numbers)
    total = sum(numbers)
    minimum = numbers[0]
    maximum = numbers[0]
    
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
            
    average = total / count
    print(count, total, minimum, maximum, f"{average:.2f}")