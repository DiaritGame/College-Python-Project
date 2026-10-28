path = "data/logs.txt"
count = 0
with open(path, "r", encoding="utf-8") as file:
    for string in file:
        string = string.lower()
        if 'error' in string:
            print(string,end='')
            count += 1
print(count)