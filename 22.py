path = 'data/score'
summ = 0
counts = 0
lst = []
with open(path, 'r', encoding="utf-8") as file:
    for string in file:
        string = string.strip()
        lst = string.split(';')
        if lst[1].isdigit():
            counts += 1
            summ += int(lst[1])
        if lst[1] == '5':
            print(lst[0])
if counts > 0:
    print(f'Средняя оценка: {summ / counts}')