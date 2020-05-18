## Right Angle Alphabetical Order
def pattern(n):
    x=65                                    #65 is ASCII value for alphabet A
    for i in range(0,n):
        ch = chr(x)
        x = x+1
        for j in range(0,i+1):
            print(ch,end="")
        print("\r")

pattern(5)

## Pyramid Characters

def pattern2(n):
    k=2*n-2
    x=65                                    #65 is ASCII value for alphabet A
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            ch = chr(x)
            print(ch,end=" ")
            x+=1
        print("\r")

pattern2(7)

## Traingle Pattern

def pattern3(n):
    k = 2 *  n - 2
    x = 65
    for i in range(0, n):
        print(end=" ")
        ch = chr(x)
        x += 1
        for j in range(0, i+1):
            print(ch, end=" ")
        print("\r")

pattern3(7)

##Diamond character Pyramid

def pattern4(n):
    print()
    k = 2 * n - 2                  #this statement prints number of spaces before printing  *
    x=65
    for i in range(0,n):            # For outer rows
        ch = chr(x)
        x = x + 1
        for j in range(0,k):        # For columns
            print(end=" ")          # Blank Spaces
        k = k - 1
        for j in range(0, i+1):     # For Asteriks
            print(ch, end=" ")     # Asteriks followed by spaces
        print("\r")                 # To get a Pyramid shape instead of coming all in single line
    k = n - 2
    x = 65
    for i in range(n,-1,-1):
        ch = chr(x)
        x = x + 1
        for j in range(k,0,-1):
            print(end=" ")
        k = k + 1
        for i in range(0, i + 1):

            print(ch,end=" ")
        print("\r")
pattern4(7)