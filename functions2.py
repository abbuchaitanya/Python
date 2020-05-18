def f1():
    print("calling f1")

def f2(f):
     f()
     print("calling f1 via f2")
f2(f1)

