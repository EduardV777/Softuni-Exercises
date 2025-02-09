from math import floor

competitor1 = int(input())
competitor2 = int(input())
competitor3 = int(input())

sumTime = competitor1 + competitor2 + competitor3

totalMin = floor(sumTime / 60)
totalSec = sumTime - (totalMin * 60)

out = f"{totalMin}:"

if totalSec < 10:
    out += f"0{totalSec}"
else:
    out += f"{totalSec}"

print(out)