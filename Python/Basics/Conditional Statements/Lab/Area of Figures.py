from math import pi

shapeType = input()
area = 0

if shapeType == "square":
    a = float(input())
    area = a * a

elif shapeType == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b

elif shapeType == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2

elif shapeType == "circle":
    r = float(input())
    area = pi * (r * r)

print(f"{area:.3f}")