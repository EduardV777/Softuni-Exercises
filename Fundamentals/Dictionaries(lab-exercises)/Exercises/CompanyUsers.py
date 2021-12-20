companies_employees={}

while True:
    command=input()
    if command!="End":
        companyFound=False
        employeeData=command.split(" -> ")
        companyName=employeeData[0]; employeeId=employeeData[1]
        for j in companies_employees:
            if j==companyName:
                companyFound=True
                try:
                    if companies_employees[j].index(employeeId)>-1:
                        break
                except:
                    companies_employees[j].append(employeeId)
                break
        if companyFound==False:
            companies_employees[companyName]=[employeeId]
    else:
        orderByCompany = sorted(companies_employees.items())
        orderByCompany = dict(orderByCompany)
        for j in orderByCompany:
            print(f"{j}")
            for k in range(0,len(orderByCompany[j])):
                print(f"-- {orderByCompany[j][k]}")
        break
