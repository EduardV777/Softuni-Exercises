n=int(input())
uniqueUsernames=set([])
while n!=0:
    user=input()
    uniqueUsernames.add(user)
    n-=1

while len(uniqueUsernames):
    print(uniqueUsernames.pop())