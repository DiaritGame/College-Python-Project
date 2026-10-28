price = int(input("Введите сумму: "))
discount = int(input("Введите скидку: "))
sum = price * (1 - discount / 100)
print(f"Итоговая цена: {sum}")