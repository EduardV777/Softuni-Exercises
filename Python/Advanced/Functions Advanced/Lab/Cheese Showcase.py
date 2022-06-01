def sorting_cheeses(**kwargs):
    output=""
    sameQuantities=False
    pieces=0

    for k in kwargs:
        if pieces==0:
            pieces=len(kwargs[k])
            for j in kwargs:
                if pieces == len(kwargs[j]) and (j!=k):
                    sameQuantities = True
                    break
            if sameQuantities==True:
                break
    print(sameQuantities)
    if sameQuantities==False:
        sortedKwargs=sorted(kwargs.items(), key=lambda x: -len(x[1]))
    else:
        sortedKwargs=sorted(kwargs.items(), key=lambda x: x[0])

    sortedKwargs=dict(sortedKwargs)

    for k in sortedKwargs:
        output+=k+"\n"
        quantities=sortedKwargs[k]
        quantities=sorted(quantities, key=lambda x: -x)
        quantities=[str(e) for e in quantities]
        sortedKwargs[k]=quantities
        for j in sortedKwargs[k]:
            output+=j+"\n"
    return output


#print(sorting_cheeses(Parmesan=[102, 120, 135],Camembert=[100, 100, 105, 500, 430],Mozzarella=[50, 125],))
#print(sorting_cheeses(Parmigiano=[165, 215],Feta=[150, 515],Brie=[150, 125]))