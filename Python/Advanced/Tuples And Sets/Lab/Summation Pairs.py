numbers=input(); targetNumber=int(input())
numbers=numbers.split(" "); numbers=[int(e) for e in numbers]
iters=0
uniquePairs=set([])

for k in range(0,len(numbers)):
    num=numbers[k]
    for j in range(0,len(numbers)):
        if j==k:
            continue
        else:
            if numbers[k]+numbers[j]==targetNumber:
                iters += 1
                pair=f"{numbers[k]}, {numbers[j]}"
                uniquePairs.add(pair)
                print(f"{numbers[k]} + {numbers[j]} = {targetNumber}")

print(f"Iterations done: {iters}")

while len(uniquePairs)!=0:
    print(f"({uniquePairs.pop()})")
