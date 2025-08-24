openTabs = int(input())
salary = int(input())
salaryDeducted = False


for i in range(0, openTabs):
    website = input()

    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        salaryDeducted = True
        break

if salaryDeducted:
    print("You have lost your salary.")
else:
    print(f"{salary}")