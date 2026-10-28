Pyt = 0
dva = 0

while True:
    a = int(input("Введите оцнку: "))
    if a == 0:
        break
    if a == 5:
        Pyt += 1
    if a == 2:
        dva += 1
print("Пятерок:", Pyt)
print("Двоек:", dva)