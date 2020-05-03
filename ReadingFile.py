# Reading an External file into Python Program
# Different modes of accessing file
# r     -   read
# w     -   write
# a     -   append
# r+    -   read / write

# If both program and file are in same path, then simple accessing by file name works

family = open("Family.txt", "r")
print(family.readable())
print(family.read())
print("--------------")
family.close()

family = open("Family.txt", "r")
print(family.readable())
print(family.readline())
print(family.readline())
print(family.read())
print("--------------")
family.close()

family = open("Family.txt", "r")
print(family.readable())
print(family.readlines())
print(family.readline())
print("--------------")
family.close()

family = open("Family.txt", "r")
print(family.readable())
print(family.readlines()[1])
print(family.readline())
print("--------------")
family.close()

family = open("Family.txt", "r")
for mem in family.readlines():
    print(mem)
print("--------------")
family.close()