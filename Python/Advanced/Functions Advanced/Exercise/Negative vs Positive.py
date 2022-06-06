nums=[int(e) for e in input().split()]

def separateNumbers(*args):
    negativeNumbersSum=0; positiveNumbersSum=0

    for k in args:
        if k<0:
            negativeNumbersSum+=k
        else:
            positiveNumbersSum+=k

    print(negativeNumbersSum)
    print(positiveNumbersSum)
    if abs(negativeNumbersSum)>positiveNumbersSum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

separateNumbers(*nums)