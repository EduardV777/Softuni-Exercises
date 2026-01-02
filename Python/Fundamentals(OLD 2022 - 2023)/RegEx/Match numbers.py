import re
findNums=re.compile(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))")
numbers=input()
validNumbers=findNums.finditer(numbers)
for m in validNumbers:
    print(m.group(), end=" ")
