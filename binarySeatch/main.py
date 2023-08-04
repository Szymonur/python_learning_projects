tab = []
import random
i = 0
while i < 100000:
    tab.append(random.randint(0,100000))
    i += 1
tab.sort()
y = tab[random.randint(0,100000)]

def binarySearch(tab, x):
    firs, last = 0, len(tab)
    if x < tab[firs] or x > tab[last-1]:
        return False
    while last-firs > 1:
        p = firs + (last - firs)//2
        if x == p or x == firs or x == last:
            return p
        if x > tab[p]:
            firs = p + 1
        else:
            last = p - 1
    return False

def linearSearch(tab, x):
    for i in range(0,len(tab)):
        if tab[i] == x:
            return i
    return False

import timeit
x = timeit.timeit('binarySearch(tab, y)', number=1000, globals = globals())
print(x)
x = timeit.timeit('linearSearch(tab, y)', number=1000, globals = globals())
print(x)




