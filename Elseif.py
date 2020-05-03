is_male =   True
is_tall =   True

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male, but tall")
else:
    print("You are either not male or not tall or both")

is_male =   True
is_tall =   False

print()
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male, but tall")
else:
    print("You are either not male or not tall or both")

is_male =   False
is_tall =   True

print()
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male, but tall")
else:
    print("You are either not male or not tall or both")

is_male =   False
is_tall =   False

print()
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are not a male, but tall")
else:
    print("You are not male and short")

