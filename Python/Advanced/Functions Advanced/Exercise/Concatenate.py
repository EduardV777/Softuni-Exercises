def concatenate(*args, **kwargs):
    txt=[e for e in args]

    for k in kwargs:
        if k in txt:
            try:
                ind=txt.index(k)
                txt[ind]=kwargs[k]
            except:
                pass #err

    for k in range(0,len(txt)):
        changed=False
        word=[e for e in txt[k]]
        for j in kwargs:
            if j in word:
                try:
                    ind = word.index(j)
                    word[ind] = kwargs[j]
                    changed=True
                except:
                    pass  # err
        if changed==True:
            txt[k]=''.join(word)


    return ''.join(txt)



print(concatenate("I", " ", "Love", " ", "Cythons",

C="P", s="", java='Java'))