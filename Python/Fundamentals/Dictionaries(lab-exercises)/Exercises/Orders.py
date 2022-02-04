products={}
while True:
     productData=input()
     if productData!="buy":
         data=productData.split(" ")
         price = float(data[1]); qty = int(data[2])
         productFound=False
         for j in products:
             if j==data[0]:
                 products[j][0]=price; products[j][1]+=qty
                 productFound=True
                 break
         if productFound==False:
             products[data[0]]=[price,qty]
     else:
        output=""
        for j in products:
            output+=f"{j} -> {products[j][0]*products[j][1]:.2f}\n"
        print(output)
        break
