a = input()
words = a.split()
count = 0

for word in words:
    clean_word = word.strip(".,!?;:").lower()
    
    if not clean_word:
        continue
        
    if clean_word.startswith("а"):
        print(clean_word)
        count += 1

if count == 0:
    print("Нет совпадений")

print(count)