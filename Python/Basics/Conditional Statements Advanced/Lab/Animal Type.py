# dog -> mammal
# crocodile, tortoise, snake -> reptile
# others -> unknown

animalType = input()

if animalType == "dog":
    print("mammal")
elif animalType == "crocodile" or animalType == "tortoise" or animalType == "snake":
    print("reptile")
else:
    print("unknown")