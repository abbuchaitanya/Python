## Generator expressions

f= range(12)
print("List comp", end=":")
q=[x+2 for x in f]
print(q)
print("Generator Exp", end=":")
r=(x+2 for x in f)
print(r)
#print(min(r))
for x in r:
    print(x)