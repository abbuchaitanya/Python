##Lambda with in user-defined functions

def a(x):
    return lambda y:x+y
t = a(9)
print(t(10))

##***************
def a(x):
    return lambda y:x-y
t = a(9)
print(t(10))
u = a(5)
print(u(34))