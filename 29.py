def word_statistics(words):
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    maxx = 0
    result = 0
    for key, values in d.items():
        if values > maxx:
            maxx = values
            result = key
    return d, result

print('Обычный вывод:')
print(word_statistics(["кот", "пёс", "кот", "лиса", "пёс", "кот"]))
print(f'\nКрасивый вывод:')

#Я решил попробовать по красивому принтануть итоговый словарь:

data = word_statistics(["кот", "пёс", "кот", "лиса", "пёс", "кот"])
counts, max_word = data  #распаковка кортежа

for word, count in counts.items(): #word - 1 составная кортежа, count - вторая
    print(f"{word}: {count}")

print(f"Самое частое слово: {max_word}")