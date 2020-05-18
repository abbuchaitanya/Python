def func1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
        function(*args, **kwargs)
        print("Welcome Home")
    return wrapper
 # py syntax or Sugar syntax. Alternative to statement func2 = func1(func2)
 # With above syntax, same example is writter Decorators.py
@func1

def func2(name):
    print (f"{name}")

func2("kumar")