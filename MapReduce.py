##Mapfunction
##Syntax : map(func, iterables)

##Example 1

def new(a):
    return a*a
x=map(new,[2,4,6,8,10])
print(x)
print(tuple(x))

## Example2

def new(a, b):
    return a*b
x=map(new,[2,4,6,8,10], [-2,-4,-6,-8,-10])
print(x)
print(tuple(x))

# example 3
## Lambda function with Mapfunction
a = [2,4,6,8,10]
b = list(map(lambda c: c+3,a))
print(b)
print(tuple(b))

#example4
#syntax: filter(func, iterables)
## Filter function with user defined function
tpl =(1, 2, 3, 4, 5, 6, 7, 8)
def new1(i):
    if i>=3:
        return i
j = filter(new1,tpl)
print(j)
print(list(j))

#example5
## Filter function with lambda function
tpl =(1, 2, 3, 4, 5, 6, 7, 8)
z = list(filter(lambda i: i>=5,tpl))
print(z)

#example 6
#Syntax: reduce(function, iterables)
##Reduce function with user defined function

from functools import reduce
def sum(x,y):
    return x + y
s = reduce(sum,[1,2,3,4,5,6])
print(s)


#example 7
##Reduce function with lambda function

t = reduce(lambda x,y: x * y, [1,2,3,4,5,6] )
print(t)

