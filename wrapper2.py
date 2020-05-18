## Wrapper using decorator functio

def f1(func):
    def wrapper():
        print("Started...")
        func()
        print("Ended")
    return wrapper

def f2():
    print("Hello, wrapper")

##f1(f2)()  ## replace this statement with below decorator

x = f1(f2)

x()
