class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, val):
        invalid = False

        for k in range(65, 91):
            for ch in val.lower():
                if ch == chr(k):
                    invalid = True

        if not val[0] == '0' or len(val) < 10 or invalid == True:
            raise ValueError("Invalid phone number!")
        else:
            self.__phone_number = val