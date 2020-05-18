def func1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome Home")
    return wrapper
 # py syntax or Sugar syntax. Alternative to statement func2 = func1(func2)
 # With above syntax, same example is writter Decorators.py
@func1

def func2():
    print("How are you doing?")

func2()