def positives(values):
    positive_numbers = []
    for x in values:
        if x >= 0:
            positive_numbers.append(x)
    return positive_numbers


values = [-2, 5, 0, 7, -1]
print(*positives(values))