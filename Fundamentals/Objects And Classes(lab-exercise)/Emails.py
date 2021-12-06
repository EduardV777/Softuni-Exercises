class email:
    def __init__(self,sender,receiver,content,is_sent=False):
        self.sender=sender
        self.receiver=receiver
        self.content=content
        self.is_sent=is_sent
    def send(self):
        self.is_sent=True
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
command=""; emails=[]
while command!="Stop":
    sender="";receiver="";content=""
    command=input()
    if command!="Stop":
        k=0; i=0
        while k<len(command):
            if command[k]!=" ":
                val=""
                for j in range(k,len(command)):
                    if command[j]!=" ":
                        val+=command[j]
                        k+=1
                    else:
                        break
                if i==0:
                    sentBy=val
                elif i==1:
                    receivedBy=val
                elif i==2:
                    message=val
                i+=1
            else:
                k+=1
        currEmail=email(sentBy,receivedBy,message)
        emails.append(currEmail)
indices=input()
k=0
while k<len(indices):
    if indices[k].isdigit():
        emails[int(indices[k])].send()
    k+=1
for k in range(0,len(emails)):
    print(emails[k].get_info())
