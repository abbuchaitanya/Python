def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(80, 140, 50))

def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

print(min_num(50, 140, 50))

def equal_num(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        return num1, num2, num3
    elif num1 == num2:
        return num1, num2
    elif num1 == num3:
        return num1, num3
    elif num2 == num3:
        return num2, num3
    else:
        return

print(equal_num(50, 150, 50))