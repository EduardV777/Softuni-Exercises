file = open("text.txt", "r")

contents = file.read()

contents = contents.split("\n")

for k in range(0,len(contents)):
    contents[k] = contents[k].replace("-", "@")
    contents[k] = contents[k].replace(",", "@")
    contents[k] = contents[k].replace(".", "@")
    contents[k] = contents[k].replace("!", "@")
    contents[k] = contents[k].replace("?", "@")

    contents[k] = contents[k].split(" ")
    contents[k].reverse()

    if k%2 == 0:
        print(" ".join(contents[k]))