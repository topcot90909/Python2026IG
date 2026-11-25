data = input().split()
filtered = []
for x in data:
    num = int(x)
    if num % 2 == 0:
        filtered.append(num)
print(filtered)
count = len(filtered)
total = sum(filtered)
print(count)
print(total)

sorted_copy = sorted(filtered)
print(sorted_copy)