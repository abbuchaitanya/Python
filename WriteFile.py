# Writing into an External file using Python Program
# Different modes of accessing file
# r     -   read
# w     -   write
# a     -   append
# r+    -   read / write

# If both program and file are in same path, then simple accessing by file name works

# Write mode, overwrites all the existing data
family = open("Family.txt", "w")
print(family.writable())
print(family.write("Grandfather -   Janaki Rami Reddy"))
print("--------------")
family.close()

# Append mode, append data at last of the file to the existing data
# \n writes line in next new line
family = open("Family.txt", "a")
print(family.writable())
print(family.write("\nGrandmother -   Krishnamma"))
print("--------------")
family.close()

# Write mode, overwrites all the existing data
family = open("index.html", "w")
print(family.writable())
print(family.write("<p>This is HTML Program</p>"))
print("--------------")
family.close()