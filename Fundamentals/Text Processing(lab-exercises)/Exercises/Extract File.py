filepath=input()
fileFullName=""
for k in range(len(filepath)-1,0,-1):
    if filepath[k]!="\\":
        fileFullName+=filepath[k]
    else:
        fileFullName=reversed(fileFullName)
        fileName=""
        for ch in fileFullName:
            fileName+=ch
        break

NameAndExt=fileName.split(".")
print(f"File name: {NameAndExt[0]}\nFile extension: {NameAndExt[1]}")
