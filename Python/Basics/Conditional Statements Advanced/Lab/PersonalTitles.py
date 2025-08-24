age = float(input())
sex = input()

if sex == "m":
    if 16 <= age:
        print("Mr.")
    else:
        print("Master")
elif sex == "f":
    if 16 <= age:
        print("Ms.")
    else:
        print("Miss")