## With Forloop
def myfunc():
    n=4
    yield n
    n = n + 4
    yield n
    n = n * 4
    yield n
k = myfunc()
for x in k:
    print(x)