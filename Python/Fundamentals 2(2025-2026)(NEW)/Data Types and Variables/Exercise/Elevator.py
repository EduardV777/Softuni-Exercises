from math import ceil

n = int(input())
cap = int(input())

courses = ceil(n / cap)

print(courses)