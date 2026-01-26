#Example
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.

from math import floor

numbers = input().split(", ")
numbers = list(map(int, numbers))

groups = [[f"{k * 10}"] for k in range(1,101)]

output = ""

def sortGroups(seq: list):

    for val in seq:
        pos = floor(val / 10)

        if val % 10 == 0:
            pos = round(val / 10) - 1

        groups[pos].append(val)

    #cleanup
    while True:
        check = False

        for k in range(0, len(groups)):
            if len(groups[k]) == 1:
                check = True
                del groups[k]
                break

        if not check:
            break

def formatOutput(listGroups: list, output: str):

    for k in listGroups:
        output += f"Group of {k[0]}'s: "
        temp = k.pop(0)
        output += f"{k}\n"
        k.insert(0, temp)
        del temp

    return output

sortGroups(numbers)
output = formatOutput(groups, output)

print(output)

del numbers