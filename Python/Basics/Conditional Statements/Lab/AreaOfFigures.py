from math import pi

shapeType = input()
s = None

if shapeType == "rectangle":
    a = float(input())
    b = float(input())

    s = a * b

elif shapeType == "triangle":
    aLength = float(input())
    h = float(input())

    s = aLength / 2 * h

elif shapeType == "square":
    aLength = float(input())

    s = aLength * aLength

elif shapeType == "circle":
    r = float(input())
    s = (r * r) * pi


print(f"{s:.3f}")