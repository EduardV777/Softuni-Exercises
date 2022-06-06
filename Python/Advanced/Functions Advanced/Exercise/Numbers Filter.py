def even_odd_filter(**kwargs):
    dictionary={}
    if 'even' in kwargs:
        dictionary['even']=[e for e in kwargs['even'] if e%2==0]
    if 'odd' in kwargs:
        dictionary['odd']=[e for e in kwargs['odd'] if e%2!=0]

    dictionary=dictionary.items()
    dictionary=sorted(dictionary, key=lambda x: -len(x[1]))
    dictionary=dict(dictionary)
    return dictionary