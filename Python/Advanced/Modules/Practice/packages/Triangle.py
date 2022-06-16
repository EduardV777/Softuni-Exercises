def print_triangle(n):
    j = 0
    i = n

    for k in range(0,n):
        if k == n-1:
            print(f"{' '*i}/{'__' * j}\\")
        else:
            print(f"{' '*(i)}/{'  ' * j}\\")

        j += 1
        i -= 1