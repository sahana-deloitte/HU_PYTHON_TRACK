n = 5
for i in range(1, n + 1):

    # Loop through columns
    for j in range(1, n + 1):

        # Printing Pattern
        if (j == n) or (i == 1) or (i == j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()