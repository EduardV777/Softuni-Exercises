orders = int(input())
total = 0

while orders:
    priceCapsule = float(input()) #[0.01 100]
    days = int(input()) # [1 31]
    capsulesPerDay = int(input()) # [1 2000]

    if (0.01 <= priceCapsule <= 100) and (1 <= days <= 31) and (1 <= capsulesPerDay <= 2000):
        total += (capsulesPerDay * priceCapsule) * days
        print(f"The price for the coffee is: ${(capsulesPerDay * priceCapsule) * days:.2f}")

    orders -= 1

print(f"Total: ${total:.2f}")