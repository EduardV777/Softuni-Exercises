happinessRates=input(); improvementFactor=int(input())
happinessRatesList=[]
k=0
while k<len(happinessRates):
    rate=""
    if happinessRates[k]!=" ":
        for j in range(k,len(happinessRates)):
            if happinessRates[j]!=" ":
                rate+=happinessRates[j]
                k+=1
            else:
                k+=1
                break
        rate=int(rate)
        happinessRatesList.append(rate)
happinessRatesIncreased=list(map(lambda x: x*improvementFactor, happinessRatesList))
avgHappiness=0
for j in range(0,len(happinessRatesIncreased)):
    avgHappiness+=happinessRatesIncreased[j]
avgHappiness/=len(happinessRatesIncreased)
totalEmployees=len(happinessRatesIncreased)
happyEmployees=list(filter(lambda y: y>=avgHappiness, happinessRatesIncreased))
if len(happyEmployees)>=len(happinessRatesIncreased)//2:
    print(f"Score: {len(happyEmployees)}/{len(happinessRatesIncreased)}. Employees are happy!")
else:
    print(f"Score: {len(happyEmployees)}/{len(happinessRatesIncreased)}. Employees are not happy!")
