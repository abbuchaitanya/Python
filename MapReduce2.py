## Example 1
## Filter function within Map function with Lambda function
c = map(lambda x:x+x, filter(lambda x:x>=4,(2,3,4,5,6)))
print(list(c))

## Example 2
## Map function within Filter function with Lambda function

d = filter(lambda x: x>=7, map(lambda x:x+x,{1,2,3,4,5,6,7}))
print(tuple(d))

## Example 2
## Map & Filter function within Reduce function with Lambda function
from functools import reduce

e = reduce(lambda x,y:x*y, map(lambda x:(x-2), filter(lambda x:(x>3),[1,2,3,4,5,6,7,8])))
print(e)
