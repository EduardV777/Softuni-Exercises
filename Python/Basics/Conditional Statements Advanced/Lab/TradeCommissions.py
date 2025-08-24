commissions = [[5,7,8,12], [4.5,7.5,10,13], [5.5,8,12,14.5]]

city = input()
sellVol = float(input())

comSize = 0
error = False

if sellVol < 0:
    print("error")
    error = True

if city == "Sofia" and not error:
    if 0 <= sellVol <= 500:
        comSize = sellVol * (commissions[0][0] / 100)
    elif 500 < sellVol <= 1000:
        comSize = sellVol * (commissions[0][1] / 100)
    elif 1000 < sellVol <= 10000:
        comSize = sellVol * (commissions[0][2] / 100)
    elif 10000 < sellVol:
        comSize = sellVol * (commissions[0][3] / 100)
elif city == "Varna" and not error:
    if 0 <= sellVol <= 500:
        comSize = sellVol * (commissions[1][0] / 100)
    elif 500 < sellVol <= 1000:
        comSize = sellVol * (commissions[1][1] / 100)
    elif 1000 < sellVol <= 10000:
        comSize = sellVol * (commissions[1][2] / 100)
    elif 10000 < sellVol:
        comSize = sellVol * (commissions[1][3] / 100)

elif city == "Plovdiv" and not error:
    if 0 <= sellVol <= 500:
        comSize = sellVol * (commissions[2][0] / 100)
    elif 500 < sellVol <= 1000:
        comSize = sellVol * (commissions[2][1] / 100)
    elif 1000 < sellVol <= 10000:
        comSize = sellVol * (commissions[2][2] / 100)
    elif 10000 < sellVol:
        comSize = sellVol * (commissions[2][3] / 100)

else:
    if not error:
        print("error")
        error = True

if not error:
    print(f"{comSize:.2f}")
