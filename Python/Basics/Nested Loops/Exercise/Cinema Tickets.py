totalTickets = 0
students = 0
standard = 0
kid = 0

while True:
    movieName = input()

    if movieName != "Finish":
        freeSeats = int(input())
        totalSeats = freeSeats
        while freeSeats != 0:
            typeTicket = input()

            if typeTicket != "End":
                totalTickets += 1
                if typeTicket == "student":
                    students += 1
                elif typeTicket == "standard":
                    standard += 1
                elif typeTicket == "kid":
                    kid += 1

                freeSeats -= 1
            else:
                break
        print(f"{movieName} - {((totalSeats - freeSeats) / totalSeats) * 100:.2f}% full.")

    else:
        print(f"Total tickets: {totalTickets}")
        print(f"{(students / totalTickets) * 100:.2f}% student tickets.")
        print(f"{(standard / totalTickets) * 100:.2f}% standard tickets.")
        print(f"{(kid / totalTickets) * 100:.2f}% kids tickets.")
        break