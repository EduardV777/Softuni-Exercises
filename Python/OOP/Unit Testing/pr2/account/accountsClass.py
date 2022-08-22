class Account:

    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if len(val) < 4:
            raise ValueError("Name is below 4 symbols!")
        else:
            self.__name = val

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, val):
        if len(val) < 6:
            raise ValueError("Password must be at least 6 symbols long.")
        else:
            self.__password = val


    def __repr__(self):
        return f"Account name: {self.name}; Account password: {self.password}"