import functools

def repeat(num):
    def decorator_repeat(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value   =   function(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(8)

def func(name):
    print(f"{name}")

func("Kumar")