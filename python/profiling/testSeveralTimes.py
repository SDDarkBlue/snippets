import timeit

source = open('test.py').read()
result = timeit.Timer(source).repeat(repeat=10, number=1)
print result
