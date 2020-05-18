##Number Pyramids

##Ascending Pyramid

def pattern1(n):
    x=0
    for i in range(0,n,):
        x=x+1
        for j in range(0,i+1):
            print(x,end="")
        print("\r")
pattern1(5)

##Descending Pyramid
def pattern(n):
    for i in range(n,0,-1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("\r")

pattern(5)

##Diamond Number Pyramid

def pattern2(n):
    k = 2 * n - 2                  #this statement prints number of spaces before printing  *
    x=0
    for i in range(0,n):            # For outer rows
        x = x + 1
        for j in range(0,k):        # For columns
            print(end=" ")          # Blank Spaces
        k = k - 1
        for j in range(0, i+1):     # For Asteriks

            print(x, end=" ")     # Asteriks followed by spaces
        print("\r")                 # To get a Pyramid shape instead of coming all in single line
    k = n - 2
    x = 0
    for i in range(n,-1,-1):
        x = x + 1
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for i in range(0, i + 1):

            print(x,end=" ")
        print("\r")


pattern2(9)