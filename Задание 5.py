a = int(input("Введите температуру: "))
if a < 0:
    print("Мороз")
elif 0 < a < 25:
    print("Нормально")
else:
    print("Жарко")