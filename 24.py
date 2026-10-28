triongels = [[3,4,5],[1,2,2],[6,8,10],[5,5,5],[7,10,12],[4,5,6],[2,3,4],[8,15,17],[9,9,12],[10,11,13]]

def sporage(summ, count, lst_sum):
    for x in triongels:
        summ = 0
        count = 0
        for i in x:
            summ += i
            count += 1
        s = summ / count
        lst_sum.append(s)
    return lst_sum

def find_max(lst_sum):
    maxx = 0
    for m in lst_sum:
        if m > maxx:
            maxx = m
    return maxx

lst_sum = []
sporage(0, 0, lst_sum)
print(find_max(lst_sum))

# Если не использовать функции:
# lst_sum = []
# for x in triongels:
#     lst_sum.append(sum(x) / len(x))
# print(max(lst_sum))