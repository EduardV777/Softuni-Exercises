n=int(input())
longestIntersection=set([])
longestIntersectionLength=0
while n:
    ranges=input()
    ranges=ranges.split("-")
    firstRange=ranges[0].split(","); firstRange=[int(e) for e in firstRange]
    secondRange=ranges[1].split(","); secondRange=[int(e) for e in secondRange]
    set1=set([]) ; set2=set([])
    for k in range(firstRange[0], firstRange[1]+1):
        set1.add(k)
    for k in range(secondRange[0], secondRange[1]+1):
        set2.add(k)
    interSet=set1.intersection(set2)
    if len(interSet)>longestIntersectionLength:
        longestIntersection=interSet
        longestIntersectionLength=len(interSet)

    n-=1

output=f"Longest intersection is {[e for e in longestIntersection]} with length {longestIntersectionLength}"
print(output)