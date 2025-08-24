from math import pow

n = int(input())

for k in range(0 , n + 1, 2):
    print(round(pow(2, k)))