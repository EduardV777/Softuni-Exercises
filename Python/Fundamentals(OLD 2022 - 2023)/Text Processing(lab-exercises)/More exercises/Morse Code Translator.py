morseMsg=input()
morseChars={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}
def DecodeMorse(messages):
    decodedmsg=[]
    messages=messages.split(" | ")
    #print(messages)
    for k in range(0,len(messages)):
        msgFragments=messages[k].split(" ")
        word = ""
        for j in range(0,len(msgFragments)):
            for i in morseChars:
                if msgFragments[j]==morseChars[i]:
                    word+=i
                    break
        decodedmsg.append(word)
    return " ".join(decodedmsg)
print(DecodeMorse(morseMsg))
