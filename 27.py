def average_marks(students):
    d = {}
    for k, v in students.items():
        if len(v) > 0:
            d[k] = sum(v) / len(v)
        else:
            d[k] = 0
    return d

print(average_marks({"Анна": [5, 4, 5], "Иван": [3, 4], "Олег": []}))


