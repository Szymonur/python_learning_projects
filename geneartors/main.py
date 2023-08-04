def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator() # zwraca jako ovbiekt, trzeba przez niego iterować

# print(sum(g)) zsumuje wszytkie wartości z yield'ów

#for i in g:
#    print(i)

value = next(g) # zwraca pierwszego yield
print(value)
value = next(g) # zwraca drugiego yield
print(value)

g2 = mygenerator()
print(sorted(g2)) # sortuje

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))

import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(10000000)))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

mygen = ( i for i in range(1000) if i % 2 == 0) # przez generator jest dużo miniejsze
mylist = [ i for i in range(1000) if i % 2 == 0] # jako zwykła tablica jest dużo większa
print(sys.getsizeof(mygen))
print(sys.getsizeof(mylist))





