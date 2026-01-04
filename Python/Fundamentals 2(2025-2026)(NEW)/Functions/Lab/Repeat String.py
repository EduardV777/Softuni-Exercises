def repeat(txt = input(), n = int(input()) ):
    newTxt = ""

    while n:
        newTxt += txt

        n -= 1

    return newTxt

print(repeat())