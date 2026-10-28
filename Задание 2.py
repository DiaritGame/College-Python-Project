age = int(input("Введите возраст: "))
ticket = int(input("Введите наличие студенческого билета: 1 - если есть, 0 - если нету: "))
if age < 25 and ticket == 1:
    print("True")
else:
    print("False")