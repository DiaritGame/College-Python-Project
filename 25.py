def count_vowels(text, c):
    for x in text:
        if x in vowels:
            c += 1
    return c

c = 0
vowels = 'аеиёоуыэюя'
text = input("Введите строку: ").lower()

print(count_vowels(text, c))
