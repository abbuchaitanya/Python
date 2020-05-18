## Create File
import os
file = open("Family2.txt", "x")
file.close()

## Write File
import os
file = open("Family2.txt",'w')
file.write("Father      -       Chaitanya Abbu\n")
file.write("Mother      -       Kanchana Eddala\n")
file.close()

##Append File
import os
file = open("Family2.txt",'a')
file.write("Daughter    -       Tanvi Abbu\n")
file.write("Son         -       Sohan Abbu\n")
file.close()
