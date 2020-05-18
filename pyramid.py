##Pyramid
def pattern(n):
#    k = 2 * n - 2                  #this statement prints number of spaces before printing  *
    k = n                           # this statement prints number of spaces before printing  *
    for i in range(0,n):            # For outer rows
        for j in range(0,k):        # For columns
            print(end=" ")          # Blank Spaces
        k = k - 1
        for j in range(0, i+1):     # For Asteriks
            print("*", end=" ")     # Asteriks followed by spaces
        print("\r")                 # To get a Pyramid shape instead of coming all in single line

pattern(10)