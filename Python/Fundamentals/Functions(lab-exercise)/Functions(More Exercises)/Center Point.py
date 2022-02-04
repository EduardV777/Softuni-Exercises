from math import floor
par1=float(input()); par2=float(input()); par3=float(input()); par4=float(input())
def CoordinatePoints(x1,y1,x2,y2):
    closestPoints=""
    x1=floor(x1); x2=floor(x2); y1=floor(y1); y2=floor(y2)
    x1Distance=0; x2Distance=0; y1Distance=0; y2Distance=0
    for k in range(abs(x1),-1,-1):
        x1Distance+=1
    for j in range(abs(x2),-1,-1):
        x2Distance+=1
    for i in range(abs(y1),-1,-1):
        y1Distance+=1
    for t in range(abs(y2),-1,-1):
        y2Distance+=1
    if x1Distance==x2Distance and y1Distance==y2Distance:
        closestPoints = f"({x1}, {y1})"
    else:
        if x1Distance<x2Distance and y1Distance<y2Distance:
            closestPoints = f"({x1}, {y1})"
        else:
            closestPoints=f"({x2}, {y2})"
    return closestPoints
print(CoordinatePoints(par1,par2,par3,par4))
