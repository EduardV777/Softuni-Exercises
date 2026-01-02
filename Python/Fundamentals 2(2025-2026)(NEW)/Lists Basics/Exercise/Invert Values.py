txt = input()

numbers = txt.split(" ")

for k in range(0, len(numbers)):
    if numbers[k].isdigit():
        numbers[k] = int(numbers[k])
    else:
        if "-" in numbers[k]:

            if numbers[k].find("-") == 0 and numbers[k].count("-") == 1:
                check = numbers[k].split("-")

                if not check[1].isdigit():
                    break
                else: numbers[k] = int(numbers[k]); del check

            else: break

    if numbers[k] < 0:
        numbers[k] *= -1

    elif numbers[k] > 0:
        numbers[k] *= -1

print(numbers)