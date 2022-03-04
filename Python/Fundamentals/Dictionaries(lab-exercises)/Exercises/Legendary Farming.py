materials={"shards":0,"fragments":0,"motes":0}
legendaryObtained=False
while True:
    if legendaryObtained==True:
        break
    materialsReceived=input()
    materialsReceived=materialsReceived.split(" ")
    qty=[int(e) for e in materialsReceived if e.isdigit()==True]
    mats=[e for e in materialsReceived if e.isdigit()==False]

    for k in range(0,len(mats)):
        if mats[k].lower()=="shards":
            materials["shards"]+=qty[k]
            if materials["shards"]>=250:
                legendaryObtained = True
                print("Shadowmourne obtained!")
                materials["shards"]-=250
                break
        elif mats[k].lower()=="motes":
            materials["motes"]+=qty[k]
            if materials["motes"]>=250:
                legendaryObtained = True
                print("Dragonwrath obtained!")
                materials["motes"]-=250
                break
        elif mats[k].lower()=="fragments":
            materials["fragments"]=+qty[k]
            if materials["fragments"]>=250:
                legendaryObtained = True
                print("Valanyr obtained!")
                materials["fragments"]-=250
                break
        else:
            doesItExist=materials.get(mats[k],"nah")
            if doesItExist=="nah":
                materials[mats[k]]=qty[k]
            else:
                materials[mats[k]]+=qty[k]

for j in materials:
    print(f"{j}: {materials[j]}")
