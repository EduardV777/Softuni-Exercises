budget = float(input())
GPUs = int(input())
CPUs = int(input())
RAMs = int(input())
sale = False
saleAmount = 0 #pct

if GPUs > CPUs:
    sale = True
    saleAmount = 15

GPUp = 250
gpuCosts = GPUs * GPUp

CPUp = gpuCosts * 0.35
RAMp = gpuCosts * 0.1

total = gpuCosts + (CPUp * CPUs) + (RAMp * RAMs)

if sale == True:
    total -= total * (saleAmount / 100)


if total <= budget:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")