print("-----General Exponent Function-----")
print(2 ** 3)
print("------------------------------")
print("--Dynamic way of Exponent using for loop--")

def raise_to_pow(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
        print(result)
    return result


print("------------------------------")
print("--Calling Function--")
print(raise_to_pow(2, 4))
print("------------------------------")
