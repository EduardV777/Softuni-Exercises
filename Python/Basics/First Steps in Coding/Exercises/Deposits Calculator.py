depositSum = float(input())
depositTime = int(input())
interestRate = float(input()) / 100

finalSum = depositSum + depositTime * ((depositSum * interestRate) / 12)

print(finalSum)