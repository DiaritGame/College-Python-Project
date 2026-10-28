s = input('Enter string: ')
lst = s.split()
no_remove = []
count = 0
for x in lst:
    if x not in no_remove:
        no_remove.append(x)
        count += 1
sorty = no_remove.sort()
a = no_remove
maxi = a.index(max(a))
del a[maxi]
print(count)
print(max(a))
print(*no_remove)

