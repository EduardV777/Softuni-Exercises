import re
spell=input()

def MakeItString(passedSpell):
    passedSpell=''.join(passedSpell)
    return passedSpell

while True:
    command=input()
    if command!="Abracadabra":
        if "Abjuration" in command:
            spell=[char for char in spell]
            spell=[char.upper() for char in spell]
            spell=MakeItString(spell)
            print(spell)
        elif "Necromancy" in command:
            spell=[char for char in spell]
            spell=[char.lower() for char in spell]
            spell=MakeItString(spell)
            print(spell)
        elif "Illusion" in command:
            command=command.split(" ")
            ind=int(command[1]); letter=command[2]
            spell=[char for char in spell]
            if ind<0 or ind>len(spell)-1:
                print("The spell was too weak.")
            else:
                spell[ind]=letter
                print("Done!")
            spell=MakeItString(spell)
        elif "Divination" in command:
            command=command.split(" ")
            subStr=command[1]; subStr2=command[2]
            spell=spell.replace(subStr,subStr2)
            print(spell)
        elif "Alteration" in command:
            command=command.split(" ")
            subStr=command[1]
            findSubStr=re.compile(rf"{subStr}")
            occurrences=findSubStr.finditer(spell)
            spell=[char for char in spell]
            for j in occurrences:
                inds=j.span()
                startInd=inds[0]; endInd=inds[1]
                while endInd>startInd:
                    del spell[startInd]
                    endInd-=1
            spell=MakeItString(spell)
            print(spell)
        else:
            print("The spell did not work!")
    else:
        break
