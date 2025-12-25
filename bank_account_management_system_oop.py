#Bank Account Management System (OOP Based)

#Features:
'''A system that can:
        Create bank accounts
        Deposit money
        Withdraw money
        Show balance
        Support different account types'''


#Coding:

#create base class : BankAccount
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully")

    def show_balance(self):
        print(f"{self.name}'s balance: ₹{self.__balance}")

    # helper method for child classes
    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance


class SavingsAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.minimum_balance = 500

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self._get_balance() - amount < self.minimum_balance:
            print("Cannot withdraw. Minimum balance of ₹500 must be maintained")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"₹{amount} withdrawn from Savings Account")

class CurrentAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self._get_balance():
            print("Insufficient balance")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"₹{amount} withdrawn from Current Account")

print("---- Savings Account ----")
savings = SavingsAccount("Vyshnav", 1000)
savings.withdraw(300)
savings.show_balance()
savings.withdraw(300)   # should fail

print("\n---- Current Account ----")
current = CurrentAccount("Vyshnav", 1000)
current.withdraw(800)
current.show_balance()
