log = []

while True:
    command = input()

    if command == "end":
        break
    else:
        if "Chat" in command:
            data = command.split()
            message = data[1]
            log.append(message)

        elif "Delete" in command:
            data = command.split()
            message = data[1]
            if message in log:
                log.remove(message)

        elif "Edit" in command:
            data = command.split()
            message = data[1]
            editedMessage = data[2]
            ind = None
            if message in log:
                ind = log.index(message)
                log[ind] = editedMessage

        elif "Pin" in command:
            data = command.split()
            message = data[1]
            ind = None
            if message in log:
                ind = log.index(message)
                log.pop(ind)
                log.append(message)

        elif "Spam" in command:
            data = command.split()
            for x in range(1, len(data)):
                log.append(data[x])


for message in log:
    print(message)