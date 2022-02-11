version=input()
version=version.split(".")
version[2]=int(version[2])+1
if version[2]==10:
    version[2]=0
    version[1]=int(version[1])+1
    if version[1]==10:
        version[1]=0
        version[0]=int(version[0])+1
version=[str(e) for e in version]
print('.'.join(version))
