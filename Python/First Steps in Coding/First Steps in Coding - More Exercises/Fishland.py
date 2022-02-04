mackerelPrice=float(input()); spratPrice=float(input()); bonito=float(input()); horseMackerel=float(input()); clams=int(input())
clamPrice=7.50; bonitoPrice=mackerelPrice+(mackerelPrice*0.6); horseMackerelPrice=spratPrice+(spratPrice*0.8)
totalCost=(bonito*bonitoPrice)+(horseMackerel*horseMackerelPrice)+(clams*clamPrice)
print(f"{totalCost:.2f}")
