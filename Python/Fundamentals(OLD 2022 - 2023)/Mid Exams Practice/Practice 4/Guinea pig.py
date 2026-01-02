foodKg=float(input()); hayKg=float(input()); coverKg=float(input()); guineaPigKg=float(input())
insufficient=False
for k in range(1,31):
    foodKg-=0.300
    if k%2==0:
        hayKg-=(foodKg*0.05)
    if k%3==0:
        coverKg-=1/3*guineaPigKg
    if foodKg<=0 or hayKg<=0 or coverKg<=0:
        print("Merry must go to the pet store!")
        insufficient=True
        break
if insufficient==False:
    print(f"Everything is fine! Puppy is happy! Food: {foodKg:.2f}, Hay: {hayKg:.2f}, Cover: {coverKg:.2f}.")
