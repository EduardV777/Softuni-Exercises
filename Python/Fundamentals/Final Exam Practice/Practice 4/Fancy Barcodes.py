import re
n=int(input())
for k in range(0,n):
    barcode=input()
    isItValid=re.compile(r"(@[#]+)([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})(@[#]+)")
    occurrences=isItValid.findall(barcode)
    if len(occurrences)==1:
        findDigits=re.compile(r"([0-9]+)")
        digits=findDigits.findall(barcode)
        if len(digits)>0:
            pg=""
            for k in range(0,len(digits)):
                pg+=digits[k]
            print(f"Product group: {pg}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
