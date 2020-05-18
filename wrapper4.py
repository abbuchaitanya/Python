## Wrapper function with *args & **kwargs arguments
## These arguments are necessary to pass values

def f1(func):
    def wrapper(*args, **kwargs):
        print("Started...")
        func(*args, **kwargs)
        print("Ended")
    return wrapper

@f1
def f2(a, b, c):
    print(a, b, "Hello, wrapper..! " , c)

f2("Hey..!" , "Hi..!", "How are you?")