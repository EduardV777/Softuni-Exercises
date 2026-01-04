def returnCharacters(ch1 = input(), ch2 = input()):

    startStop = [ord(ch1) + 1, ord(ch2)]
    output = [chr(k) for k in range(startStop[0], startStop[1])]

    return " ".join(output)

print(returnCharacters())
