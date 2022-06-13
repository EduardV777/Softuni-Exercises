import os

while True:
    command = input()

    if command != "End":
        if 'Create' in command:
            command = command.split("-")
            fileName = command[1]

            #content is deleted upon opening the file in writing mode or create a new file
            createFile = open(f'{fileName}', "w")
            createFile.close()

        elif 'Add' in command:
            command = command.split("-")

            fileName = command[1]
            content = command[2]

            file = open(f'{fileName}', 'a')
            file.write(content+"\n")
            file.close()

        elif 'Replace' in command:
            command = command.split("-")
            fileName = command[1]
            oldString = command[2]
            newString = command[3]

            if not os.path.exists(f'{fileName}'):
                print("An error occurred")
            else:
                fileRead = open(f'{fileName}', 'r')
                content = fileRead.read()

                fileWrite = open(f'{fileName}', 'w')
                content = content.replace(oldString, newString)
                fileWrite.write(content)

                fileRead.close()
                fileWrite.close()

        elif "Delete" in command:
            command = command.split("-")
            fileName = command[1]

            if not os.path.exists(f'{fileName}'):
                print("An error occurred")
            else:
                os.remove(f'{fileName}')

    else:
        break