import math

triongels = [[3,4,5],[1,2,2],[6,8,10],[5,5,5], [7,10,12],[4,5,6],[2,3,4],[8,15,17], [9,9,12],[10,11,13]]

def sporage():
    sqares = []
    for x in triongels:
        a = x[0]
        b = x[1]
        c = x[2]
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        sqares.append(s)
    return sqares

def find_max(sqares):
    maxx = 0
    for m in sqares:
        if m > maxx:
            maxx = m
    return maxx

sqares = sporage()
print(find_max(sqares))

# triongels = [[3,4,5],[1,2,2],[6,8,10],[5,5,5], [7,10,12],[4,5,6],[2,3,4],[8,15,17], [9,9,12],[10,11,13]]
# lst_sum = []
# for x in triongels:
#     lst_sum.append(sum(x) / len(x))
# print(max(lst_sum))
