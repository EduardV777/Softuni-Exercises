targets=input()
targets=targets.split(" "); targets=[int(e) for e in targets]
shotTargetsValues=[]
shotTargets=0
while True:
    ind=input()
    if ind!="End":
        ind=int(ind)
        if ind>=len(targets):
            continue
        if targets[ind]!="-1":
            targetVal=targets[ind]; shotTargets+=1
            targets[ind]="-1"
            for k in range(0,len(targets)):
                if str(targets[k])!="-1":
                    if targetVal<targets[k]:
                        targets[k]-=targetVal
                    else:
                        targets[k]+=targetVal
    else:
        targets=[str(e) for e in targets]
        print(f"Shot targets: {shotTargets} -> {' '.join(targets)}")
        break
