# "{importance}-{note}".


def toDoList():
    tasks = []

    while True:

        task = input()

        if task != "End":
            task = task.split("-")
            imp = int(task[0])
            note = task[1]

            if len(tasks) == 0:
                tasks.append([imp, note])
            else:
                foundPlace = False

                for j in range(0,len(tasks)):
                    if tasks[j][0] > imp:
                        tasks.insert(j + 1, tasks[j])
                        tasks.pop(j)
                        tasks.insert(j, [imp, note])
                        foundPlace = True
                        break

                if not foundPlace:
                    tasks.append([imp, note])

        else:
            break

    tasks = [k[1] for k in tasks]
    print(tasks)

    return

toDoList()