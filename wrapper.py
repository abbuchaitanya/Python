def f1(func):
    def wrapper():
        print("Started...")
        func()
        print("Ended")
    return wrapper

def f2():
    print("Hello, wrapper")

f1(f2)()