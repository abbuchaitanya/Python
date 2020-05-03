def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translate   =   translate   +   "s"
        else:
            translate   =   translate   +   letter
    return translate

print(translate(input("Enter a phrase: ")))

def translate2(phrase):
    translate = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translate = translate + "S"
            else:
                translate = translate + "s"
        else:
            translate = translate + letter
    return translate

print(translate2(input("Enter a phrase: ")))