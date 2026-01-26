words = input().split(" ")
palindrome = input()

def findPalindromes(seq: list, pal: str):
    foundPals = []

    for val in seq:
        revVal = [val[k] for k in range(len(val) - 1,-1,-1)]
        revVal = "".join(revVal)

        if revVal == val:
            foundPals.append(val)

    soughtPal = foundPals.count(pal)

    return foundPals, soughtPal

res = findPalindromes(words, palindrome)

print(f"{res[0]}\nFound palindrome {res[1]} times")