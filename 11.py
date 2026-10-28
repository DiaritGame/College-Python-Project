a = int(input("Введите число: "))
b = 1
while True:
    if a % b == 0:
        print(b)
    b += 1
    if a == b-1:
        break
