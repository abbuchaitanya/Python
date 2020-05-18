## decoarator example 2 - run time

import time

def timer(func):
    def wrapper():
        before  =   time.time()
        func()
        print("Function took: ", time.time() - before)

    return wrapper

@timer
def run():
    time.sleep(3)

run()