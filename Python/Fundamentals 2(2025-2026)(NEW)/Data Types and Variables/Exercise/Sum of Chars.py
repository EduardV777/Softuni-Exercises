n = int(input())
sum = 0

while n:
    character = input()
    codeASCII = ord(character)
    sum += codeASCII

    n -= 1

print("The sum equals: " + str(sum))