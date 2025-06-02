money = float(input())
depositMonths = int(input())
APR = float(input())

totalSum = money + depositMonths * ((money * (APR / 100)) / 12)

print(totalSum)