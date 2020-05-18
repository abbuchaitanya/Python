## Decorator Function

def check(func):                                        #Step 4
    def inside(a, b):                                   #Step 5
        if b == 0:                                      #Step 6
            print("can't divided by zero")
            return
        func(a, b)                                      #Step 7
    return inside

def div(a, b):                                          #Step 2
    return a / b                                        #Step 8

div = check(div)      ## Decorator function             #Step 3

print(div(10, 5))                                       #Step 1
