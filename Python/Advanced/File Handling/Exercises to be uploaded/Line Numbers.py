file = open("text.txt", "r")
writeTo = open("output.txt", "w")

contents = file.read()

contents = contents.split("\n")

for k in range(0, len(contents)):
    letters = 0
    punctuation = 0

    for j in range(0, len(contents[k])):
        if (97 <= ord(contents[k][j]) <= 122) or (65 <= ord(contents[k][j]) <= 90):
            letters += 1

        elif contents[k][j] == "." or contents[k][j] == "," or contents[k][j] == "'" or contents[k][j] == "-":
            punctuation += 1

    outputRow = f"Line {k+1}: {contents[k]} ({letters})({punctuation})\n"
    writeTo.write(outputRow)

writeTo.close()