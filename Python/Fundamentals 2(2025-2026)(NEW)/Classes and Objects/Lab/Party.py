class Party:

    def __init__(self):
        self.people = []
        self.visitors()

    def printVisitors(self):
        print(f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}")

    def visitors(self):

        while True:
            name = input()

            if not name == "End":
                self.people.append(name)
            else:
                break

        self.printVisitors()

# partyVar = Party()