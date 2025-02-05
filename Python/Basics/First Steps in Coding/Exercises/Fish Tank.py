lengthCM = int(input())
widthCM = int(input())
heightCM = int(input())
pctTaken = float(input()) / 100

tankSpaceCM = lengthCM * widthCM * heightCM; tankSpaceCM -= tankSpaceCM * pctTaken
litersAvailable = tankSpaceCM / 1000

print(litersAvailable)
