from project.dvd import DVD
from project.customer import Customer

class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def dvd_capacity(self):
        return 15

    def customer_capacity(self):
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
    
    def rent_dvd(self, customer_id: int, dvd_id: int):
        alreadyRented = False

        for j in range(0, len(self.customers)):
            for k in range(0, len(self.customers[j].rented_dvds)):
                if self.customers[j].rented_dvds[k].id == dvd_id:
                    alreadyRented = True
                    break
            if alreadyRented == True:
                break

        if alreadyRented != True:
            for j in range(0, len(self.customers)):
                if self.customers[j].id == customer_id:
                    dvdName = ""
                    for k in range(0, len(self.customers[j].rented_dvds)):
                        if self.customers[j].rented_dvds[k].id == dvd_id:
                            dvdName = self.customers[j].rented_dvds[k].name
                            alreadyRented = True
                    if alreadyRented == True:
                        return f"{self.customers[j].name} has already rented {dvdName}"
                    else:
                        dvdInstance = 0
                        for k in range(0, len(self.dvds)):
                            if self.dvds[k].id == dvd_id:
                                dvdInstance = self.dvds[k]
                                break

                        if self.customers[j].age < dvdInstance.age_restriction:
                            return f"{self.customers[j].name} should be at least {dvdInstance.age_restriction} to rent this movie"
                        else:
                            
                            self.customers[j].rented_dvds.append(dvdInstance)
                            dvdInstance.is_rented = True
                            return f"{self.customers[j].name} has successfully rented {dvdInstance.name}"
        else:
            return "DVD is already rented"

    def return_dvd(self, customer_id, dvd_id):
        for k in range(0, len(self.customers)):
            if self.customers[k].id == customer_id:

                for j in range(0, len(self.customers[k].rented_dvds)):
                    if self.customers[k].rented_dvds[j].id == dvd_id:
                        dvdName = self.customers[k].rented_dvds[j].name
                        del self.customers[k].rented_dvds[j]
                        return f"{self.customers[k].name} has successfully returned {dvdName}"
                
                return f"{self.customers[k].name} does not have that DVD"

    def __repr__(self):
        output = ""

        for k in range(0, len(self.customers)):
            output += self.customers[k].__repr__() + "\n"

        for k in range(0, len(self.dvds)):
            output += self.dvds[k].__repr__()
            if k != len(self.dvds) - 1:
                output += "\n"

        return output