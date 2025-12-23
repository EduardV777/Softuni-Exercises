savings = 0

while True:
    destination = input()

    if destination != "End":
        minBudget = float(input())

        while True:
            sum = float(input())
            savings += sum

            if savings >= minBudget:
                print(f"Going to {destination}!")
                break

        savings = 0
    else:
        break