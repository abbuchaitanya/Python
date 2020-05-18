## Generators

def new(dict):
    for x,y in dict.items():
        yield x,y
a = {1:"Hi", 2:"Hey", 3:"Hello", 4:"Bye"}
b = new(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
#print(next(b))   ##--- throws error, becasue it reached.
print("Iteration reached")

def mynew(i):
    while i<=7:
        yield i
        i+=1
j = mynew(1)
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))
print("Iteration reached")

def myfunc():
    n=4
    yield n
    n = n + 4
    yield n
    n = n * 4
    yield n
k = myfunc()
print(next(k))
print(next(k))
print(next(k))
print("Iteration reached")

