# This program to demo handling exceptions & errors using "Try & Except" function

# Without error handling.
# To test, uncomment below code and try with other than integer
#number = int(input("Enter a number: "))
#print(number)

#print("------------------------------")

# With error handling
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

print("------------------------------")

# With error handling on specific type
try:
#    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero is not possible")
except ValueError as err:
    print(err)
