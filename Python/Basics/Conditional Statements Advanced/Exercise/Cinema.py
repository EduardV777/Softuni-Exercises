projectionType = input()
r = int(input())
c = int(input())
earnings = 0
ticketCost = 0

if projectionType == "Premiere":
    ticketCost = 12.00
elif projectionType == "Normal":
    ticketCost = 7.50
elif projectionType == "Discount":
    ticketCost = 5.00


totalSeats = r * c
earnings = ticketCost * totalSeats

print(f"{earnings:.2f} leva")