## Left Start Pattern

def pattern(n):
    k = 2 * n -2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = - 1
    for i in range(n-1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

pattern(10)

## Diamond Pyramid
def pattern2(n):
#    k = 2 * n - 2                  #this statement prints number of spaces before printing  *
    k = n                           # this statement prints number of spaces before printing  *
    for i in range(0,n):            # For outer rows
        for j in range(0,k):        # For columns
            print(end=" ")          # Blank Spaces
        k = k - 1
        for j in range(0, i+1):     # For Asteriks
            print("*", end=" ")     # Asteriks followed by spaces
        print("\r")                 # To get a Pyramid shape instead of coming all in single line

def pattern3(n):
#    k = 2 * n - 2
    k = n - 8
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for i in range(0, i + 1):
            print("*",end=" ")
        print("\r")


pattern2(8)
pattern3(8)