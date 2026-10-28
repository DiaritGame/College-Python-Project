a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
oper = input("Выберите действие(+, -, *, /): ")

if oper == "+":
    print(a + b)
elif oper == "-":
    print(a - b)
elif oper == "*":
    print(a * b)
elif oper == "/":
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя")
else:
    print("Ошибка")