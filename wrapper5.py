## Wrapper function with *args & **kwargs arguments and returning values
## These arguments are necessary to pass values
## using decorator more than once

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started...")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper

@f1
def f2(a, b, c):
    print(a, b, "Hello, wrapper..! ", c)

f2("Hey..!" , "Hi..!", "How are you?")

@f1
def f3(x,y):
    return x + y
print(f3(5, 5))