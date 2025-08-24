length = int(input())       # in centimeters
width = int(input())
height = int(input())

takenSpace = float(input()) / 100

capacity = (length * width * height) * 0.001
waterRequired = capacity - (capacity * takenSpace)

print(waterRequired)