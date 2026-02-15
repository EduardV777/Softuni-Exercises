class Email:

    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")

emails = []

def getData():

    while True:

        emailData = input()

        if not emailData == "Stop":
            emailData = emailData.split(" ")
            emails.append(Email(emailData[0], emailData[1], emailData[2]))

        else:
            break

    return

def sendProcess():

    sentEmailsInd = input().split(", ")
    sentEmailsInd = list(map(int, sentEmailsInd))

    for k in sentEmailsInd:
        emails[k].send()

    return

def showData():

    for k in emails:
        k.get_info()


getData()
sendProcess()
showData()