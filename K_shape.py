for i in range(0,11):
    for j in range(0,11):
        if j == 0 or i - j == 5 or i + j == 5:
            print("K",end=" ")
        else:
            print(end=" ")
    print()
