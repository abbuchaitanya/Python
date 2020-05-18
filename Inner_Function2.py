def func1():
    print("This is first function")
    def func2():
        print("this is first child function")
    def func3():
        print("This is second child function")

    func2()
    func3()
func1()
