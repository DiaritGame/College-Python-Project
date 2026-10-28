s = 0
k = 0

while True:
    a = int(input("Введите число: "))
    if a == 0:
        break
    if a > 0:
        s += a
        k += 1
print(s / k)