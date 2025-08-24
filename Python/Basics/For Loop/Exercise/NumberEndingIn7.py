from math import floor

for k in range(1, 1001):
    if round(( (k / 10) - (floor(k / 10)) ) * 10) == 7:
        print(k)