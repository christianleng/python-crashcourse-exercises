n = 5
for i in range(n):
    for y in range(i+1):
        if i == n-1 or y == 0 or y == i:
            print("#", end="")
        else:
            print(" ", end="")
    print('')
