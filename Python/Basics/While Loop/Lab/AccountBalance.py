balance = 0

while True:
    operation = input()

    if operation != "NoMoreMoney":

        if float(operation) < 0:
            print("Invalid operation!")
            break

        balance += float(operation)
        print(f"Increase: {float(operation):.2f}")

    else:
        break

print(f"Total: {balance:.2f}")