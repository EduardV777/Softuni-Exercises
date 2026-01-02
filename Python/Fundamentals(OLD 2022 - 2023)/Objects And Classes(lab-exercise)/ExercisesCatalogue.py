class Catalogue:
    products=[]
    def __init__(self,name):
        self.catName=name
    def add_product(self,prodStr):
        self.products.append(prodStr)
    def get_by_letter(self,firstLetter):
        byLetter=map(lambda x: x if x[0]==f"{firstLetter}" else '',self.products)
        byLetter=list(byLetter)
        k=0
        while k<len(byLetter):
            if byLetter[k]=='':
                del byLetter[k]
            else:
                k+=1
        return byLetter
    def __repr__(self):
        self.products.sort()
        output=f"Items in the {self.catName} catalogue:\n"
        for k in range(0,len(self.products)):
            output+=self.products[k]+"\n"
        return output

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
