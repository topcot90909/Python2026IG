data = input().split()

if not data:
    print("Нет данных")
else:
    numbers = [int(x) for x in data]
    max_val = max(numbers)
    positions = []
    
    for index, value in enumerate(numbers):
        if value == max_val:
            positions.append(index)
            
    print(positions)