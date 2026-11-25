n = int(input())
count = 0
total = 0
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        count += 1
        total += num

print(count)
print(total)