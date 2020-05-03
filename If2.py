is_male =   True
is_tall =   False

if is_male or is_tall:
    print("You are a Male and not tall.")
else:
    print("You are neither of them")

is_male =   False
is_tall =   False

print()
if is_male or is_tall:
    print("You are a Male or tall or both.")
else:
    print("You are neither of them")

is_male =   True
is_tall =   True

print()
if is_male and is_tall:
    print("You are a tall Male.")
else:
    print("You are either Male or tall")
