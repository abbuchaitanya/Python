## Number Stream
a = range(100)
b = (x for x in a)
print(b)
for y in b:
    print(y)

## Odd Numbers
c = range(1,100,2)
d = ( x for x in c)
print("Odd Numbers")
print(d)
for y in d:
    print(y)

## Even Numbers
c = range(2,100,2)
d = ( x for x in c)
print("Even Numbers")
print(d)
for y in d:
    print(y)
