n = int(input())
values = []
pcts = [0,0,0,0,0] #<200  [200,399]  [400,599] [600,799] [800>inf]

for k in range(0, n):
    values.append(int(input()))

    if k == n - 1:
        minimum = 0
        maximum = 200
        for i in range(0, 5):
            if 0 <= i <= 3:
                x = [values[c] for c in range(0,len(values)) if minimum <= values[c] < maximum]
            else:
                x = [values[c] for c in range(0, len(values)) if minimum <= values[c]]

            pcts[i] = (len(x) / n )* 100
            minimum += 200
            maximum += 200

for pct in pcts:
    print(f"{pct:.2f}%")