def smallest(a = int(input()), b = int(input()), c = int(input()) ):

    smallest = a

    if smallest > b:
        smallest = b

    if smallest > c:
        smallest = c

    return smallest

print(smallest())