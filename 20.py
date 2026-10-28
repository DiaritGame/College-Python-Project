s = input('Enter word for find: ')
path = "data/article.txt"
count = 0
with open(path, "r", encoding="utf-8") as file:
    for string in path:
        line = file.readline()
        if s in line:
            count += 1
print(count)