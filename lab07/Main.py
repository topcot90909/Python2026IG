from functions import sum_digits, average, normalize_text, select_numbers

# 1. sum_digits
num = int(input())
print(sum_digits(num))

# 2. average
data_str = input()
if data_str.strip():
    nums = [int(x) for x in data_str.split()]
else:
    nums = []

avg = average(nums)
if avg is None:
    print("Нет данных")
else:
    print(avg)

# 3. normalize_text
text = input()
print(normalize_text(text))

# 4. select_numbers
threshold = int(input())
filtered_nums = select_numbers(nums, threshold)
print(filtered_nums)