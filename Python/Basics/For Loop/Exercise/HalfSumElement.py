n = int(input())

found = False

values = []

for k in range(0,n):
    values.append(int(input()))

    if k == n - 1:
        for i in range(0, len(values)):
            if values[i] == sum(values) - values[i]:
                print(f"Yes\nSum = {values[i]}")
                found = True
                break

if found == False:
    print(f"No\nDiff = {abs( max(values) - (sum(values) - max(values)) )}")