# Decorators example 1 - Class/Methods

import time
def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("Run")

t   =   Test()
t.decorated_method()

