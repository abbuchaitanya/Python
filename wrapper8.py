## Decorator example 3 - Log text

import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("logfile.txt", "a") as f:
            f.write("called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val =   func(*args, **kwargs)
        return val

    return wrapper

@log
def run(a, b, c=9):
    print(a+b+c)

# run(10, b = 7, c=9)
# run(10, 7, c=9)
# run(a = 10, b = 7, c=9)
# run(10, 7, 5)
run(10, 7)