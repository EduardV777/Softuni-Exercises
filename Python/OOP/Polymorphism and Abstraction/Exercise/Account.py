class Account:

    def __init__(self, owner: str, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.balance = 0

    @property
    def balance(self):
        transactionsTotal = 0

        for amount in self._transactions:
            transactionsTotal += amount
        
        self.__balance = self.amount + transactionsTotal
        return self.__balance

    @balance.setter
    def balance(self, val):
        self.__balance = val


    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        else:
            self._transactions.append(amount)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            account.add_transaction(amount_to_add)
            return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, ind):
        return self._transactions[ind]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        newAcc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)

        for amount in self._transactions + other._transactions:
            newAcc._transactions.append(amount)
        
        return newAcc



acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
print(Account.validate_transaction(acc3, -120))