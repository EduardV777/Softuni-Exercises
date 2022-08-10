class DVD:

    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def from_date(id: int, name: str, date: str, age_restriction: int):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = int(date.split(".")[1])
        month = months[month - 1]
        year = date.split(".")[2]

        return DVD(name, id, year, month, age_restriction)

    def __repr__(self):
        rentedStatus = "not rented"

        if self.is_rented == True:
            rentedStatus = "rented"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rentedStatus}"