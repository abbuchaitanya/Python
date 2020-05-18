## Create File
import os
file = open("Family3.txt", "x")
file.write("Hi Everyone")
file.close()

## Delete File
import os
if  os.path.exists("Family3.txt"):
    os.remove("Family3.txt")                # os.rmdir is used to remove a folder
else:
    print("File doesn't exists")
