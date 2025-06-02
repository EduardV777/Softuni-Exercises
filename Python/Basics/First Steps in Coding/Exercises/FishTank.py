aquaLengthCm = int(input())
aquaWidthCm = int(input())
aquaHeightCm = int(input())
takenSpacePct = float(input())


aquaCapacity = aquaHeightCm * aquaWidthCm * aquaLengthCm
aquaCapacity -= aquaCapacity * (takenSpacePct / 100)

print(aquaCapacity / 1000)