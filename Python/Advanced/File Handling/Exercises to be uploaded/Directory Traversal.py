import os

foundFilesByExtensions = {}
output = ""

filesInFolder = os.listdir('./Example')

for k in range(0,len(filesInFolder)):
    fileName = filesInFolder[k]
    fileName = fileName.split(".")

    extension = "."+fileName[1]

    if extension not in foundFilesByExtensions:
        foundFilesByExtensions[extension] = [fileName[0]+extension]
    else:
        foundFilesByExtensions[extension].append(fileName[0]+extension)

foundFilesByExtensions = foundFilesByExtensions.items()

foundFilesByExtensions = sorted(foundFilesByExtensions, key=lambda x: x[0])

foundFilesByExtensions = dict(foundFilesByExtensions)

for ext in foundFilesByExtensions:
    print(ext)
    foundFilesByExtensions[ext].sort()
    
    for file in foundFilesByExtensions[ext]:
        print(f"- - - {file}")