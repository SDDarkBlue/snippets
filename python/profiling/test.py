import random

def sumArray():
    a = []
    for i in range(1000000):
        a.append(random.random())
    sum(a)

def sumArray2():
    a = []
    for i in range(1000000):
        a.append(random.random())
    s = 0
    for i in a:
        s += i

sumArray2()
