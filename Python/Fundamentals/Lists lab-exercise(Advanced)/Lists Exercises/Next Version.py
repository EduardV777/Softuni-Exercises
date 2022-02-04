def IncreaseVersion(versionL):
    if versionL[2]+1>9:
        versionL[2]=0
        if versionL[1]+1>9:
            versionL[1]=0
            versionL[0]+=1
        else:
            versionL[1]+=1
    else:
        versionL[2]+=1
    for j in range(0,len(versionL)):
        versionL[j]=str(versionL[j])
def main():
    version=input()
    versionL=[]
    k=0
    while k<len(version):
        n=""
        if version[k]!=".":
            for j in range(k,len(version)):
                if version[j]!=".":
                    n+=version[j]
                    k+=1
                else:
                    break
            n=int(n)
            versionL.append(n)
        else:
            k+=1
    IncreaseVersion(versionL)
    print(".".join(versionL))
main()
