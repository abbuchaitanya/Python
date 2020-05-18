## Wrapper with Decorator syntax

def f1(func):
    def wrapper():
        print("Started...")
        func()
        print("Ended")
    return wrapper

@f1
def f2():
    print("Hello, wrapper")

#x = f1(f2) ## replaced with decorator syntax above f2()

f2()