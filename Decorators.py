def func1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome Home")
    return wrapper

def func2():
    print("How are you doing?")

func2       =       func1(func2)

func2()