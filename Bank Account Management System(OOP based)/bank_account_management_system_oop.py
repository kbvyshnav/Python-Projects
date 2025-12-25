#Bank Account Management System (OOP Based)
'''Features:
    A system that can:
        Create bank accounts
        Deposit money
        Withdraw money
        Show balance
        Support different account types'''

#Code:

from abc import ABC, abstractmethod

# Abstract base class
class BankAccount(ABC):

    def __init__(self, name, balance):
        # Public attribute: account holder name
        self.name = name

        # Private attribute: balance
        self.__balance = balance

    def deposit(self, amount):
        # Validate deposit amount
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    # Abstract method
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Public method to safely display balance
    def show_balance(self):
        print(f"{self.name}'s balance: ₹{self.__balance}")

    # Protected helper method
    # Used by child classes to READ balance safely
    def _get_balance(self):
        return self.__balance

    # Protected helper method
    # Used by child classes to UPDATE balance safely
    def _set_balance(self, new_balance):
        self.__balance = new_balance


# Inherits from BankAccount
class SavingsAccount(BankAccount):

    def __init__(self, name, balance):
        # Call parent constructor to initialize name and balance
        super().__init__(name, balance)

        # Savings account specific rule
        self.minimum_balance = 500


    # Overriding withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")

        elif self._get_balance() - amount < self.minimum_balance:
            print("Cannot withdraw. Minimum balance of ₹500 must be maintained")

        else:
            self._set_balance(self._get_balance() - amount)
            print(f"₹{amount} withdrawn from Savings Account")


# CurrentAccount from BankAccount
class CurrentAccount(BankAccount):

    def __init__(self, name, balance):
        # Reuse parent initialization
        super().__init__(name, balance)


    # Overriding withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self._get_balance():
            print("Insufficient balance")

        else:
            self._set_balance(self._get_balance() - amount)
            print(f"₹{amount} withdrawn from Current Account")


# Polymorphism in action:
# Different account types stored in a single list
accounts = [
    SavingsAccount("Vy", 1000),
    CurrentAccount("Anu", 3000)
]


# Same method call behaves differently based on object type
for acc in accounts:
    acc.withdraw(700)
    acc.show_balance()
    print("--------")
