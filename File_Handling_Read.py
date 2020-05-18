## File Reading

import os

# If file and program directory are same, no need to specify full path.
# By default system will consider read action, if we dont specify
# By default system will consider text format, if we dont specify
file = open("Family.txt")
print(file.read())              # read() function reads all content
file.close()

print("**************************************")
import os
file = open("Family.txt")
print(file.read(6))             # read(n) function reads n characters of available in current line
file.close()

print("**************************************")

import os
file = open("Family.txt")
print(file.readline())                      # readline() function reads current line of file
file.close()

print("**************************************")
import os
file = open("Family.txt")
print(file.readlines()[3])                  # readlines()[n] function reads nth index position line
file.close()

print("**************************************")
import os
file = open("Family.txt", "r")
for line in file:
    print(line)                             # For loop is efficient way of reading lines
file.close()

