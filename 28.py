def group_by_mark(students):
    d = {}
    for k, v in students.items():
        if v not in d:
            d[v] = [k]
        else:
            d[v].append(k)
    return d
print(group_by_mark({"Аня": 5, "Игорь": 4, "Лена": 5}))