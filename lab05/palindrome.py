a = input()
clean_a = a.lower().replace(" ", "")

if not clean_a:
    print("Нет текста")
else:
    if clean_a == clean_a[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")