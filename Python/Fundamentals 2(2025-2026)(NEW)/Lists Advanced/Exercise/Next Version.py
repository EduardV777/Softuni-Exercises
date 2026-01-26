# "{n1}.{n2}.{n3}" Numbers cannot be greater than 9

version = input().split(".")

def findNextVersion(val: list):
    val = int("".join(val))
    val += 1

    val = str(val)
    val = [k for k in val]; val = ".".join(val)

    return val

version = findNextVersion(version)

print(version)