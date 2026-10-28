s = input("Введите строку: ")
a = True

for i in range(len(s)):
    if s[i] != s[len(s) - 1 - i]:
        a = False
if a:
    print("Палиндром")
else:
    print("Не палиндром")