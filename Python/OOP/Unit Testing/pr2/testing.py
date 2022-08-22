import unittest
from account.accountsClass import Account


class TestingAccounts(unittest.TestCase):

    def __init__(self, account: Account):
        self.account = account

    def test_name_forbidden_words(self):
        self.assertNotIn('admin', self.account.name.lower(), "Forbidden word found in name - 'admin'")
        self.assertNotIn('moderator', self.account.name.lower(), "Forbidden word found in name - 'moderator'")
        print("[Pass 1]")
    def test_pass_disallowed_symbols(self):
        validPass = True
        try:
            self.assertNotIn('+', self.account.password)
        except AssertionError:
            validPass = False
        finally:
            self.assertTrue(validPass, "Pass check test success")

        print("[Pass 2]")

#accounts for testing
testingAcc = Account("Velkovadmin", "11121112")
testingAcc2 = Account('Velkov', "1112111+2")
testingAcc3 = Account('Velkov', '11121112')
#accounts for testing


print("Account created!")
print(testingAcc3)
print("Testing starts...\n")

testInit = TestingAccounts(testingAcc3)
testInit.test_name_forbidden_words()
testInit.test_pass_disallowed_symbols()