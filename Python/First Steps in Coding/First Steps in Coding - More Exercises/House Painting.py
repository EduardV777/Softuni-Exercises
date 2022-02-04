x=float(input()); y=float(input()); h=float(input())
greenPaint=0; redPaint=0
LeftRight=(x*y+x*y)-(1.5*1.5+1.5*1.5); FrontRear=(x*x+x*x)-(1.2*2)
RoofTriangles=(x*h/2)+(x*h/2); RoofSquares=(x*y+x*y)
MainHouseArea=LeftRight+FrontRear; RoofHouseArea=RoofTriangles+RoofSquares
greenPaint=(MainHouseArea/3.4)*1; redPaint=(RoofHouseArea/4.3)
print(f"{greenPaint:.2f}\n{redPaint:.2f}")
