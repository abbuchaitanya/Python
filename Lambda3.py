## Lambda within filter()
## syntax -- filter(function, iterables)

print("****** filter function ******")

mylist  =   [0,1,2,3,4,5,6,7,8,9]
newlist = list(filter(lambda a:(a/3==2),mylist))  ## to print output in list format, we used list method
print(newlist)

## Lambda within map()
##syntax -- map(function,iterables)
print("****** Map function ******")
newlist    =   list(map(lambda a:(a/3!=2), mylist))
print(newlist)

## Lambda within reduce()
## syntac -- reduce(function, sequence)
print("****** reduce function ******")

import functools
print(functools.reduce(lambda a,b:a+b,mylist))

## Lambda usage in Algebra expressions

## Linear Equations - Equations with degree 1
print("****** Linear Equations ******")
s=lambda a:a*a
print(s(5))

#3x+4y
d = lambda x,y:(3*x+4*y)
print(d(3,3))

## Quadratic Equation
#print("\n")
print("****** Quadratic Equations ******")
# (a+b)^2
q = lambda a,b:(a+b)**2
print(q(2,3))
