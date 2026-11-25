a = input().split()
original = [int(x) for x in a]
transformed = [abs(x) for x in original]

print(original)
print(transformed)