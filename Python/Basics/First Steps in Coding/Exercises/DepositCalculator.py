deposit = float(input())
depositTime = int(input())
APR = float(input())

finalAmount = deposit + depositTime * ((deposit * (APR / 100)) / 12)

print(finalAmount)