n = int(input())

values = []

for k in range(0, n):
    number = int(input())

    values.append(number)

print(f"Max number: {max(values)}\nMin number: {min(values)}")