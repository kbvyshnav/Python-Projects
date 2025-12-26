#MENU-DRIVEN BANK ACCOUNT CLI

from abc import ABC, abstractmethod


# -------------------- ABSTRACT BASE CLASS --------------------
class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"{self.name}'s balance: ₹{self.__balance}")

    # Protected helpers for child classes
    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance


# -------------------- SAVINGS ACCOUNT --------------------
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


# -------------------- CURRENT ACCOUNT --------------------
class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self._get_balance():
            print("Insufficient balance")
        else:
            self._set_balance(self._get_balance() - amount)
            print(f"₹{amount} withdrawn from Current Account")


# -------------------- MENU-DRIVEN CLI --------------------
def main():
    print("Welcome to Bank Account System")

    name = input("Enter account holder name: ")
    balance = int(input("Enter initial balance: "))

    print("\nSelect Account Type:")
    print("1. Savings Account")
    print("2. Current Account")

    acc_type = input("Enter choice (1/2): ")

    if acc_type == "1":
        account = SavingsAccount(name, balance)
    elif acc_type == "2":
        account = CurrentAccount(name, balance)
    else:
        print("Invalid account type")
        return

    while True:
        print("\n----- MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = int(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            print("Thank you for using the bank system")
            break

        else:
            print("Invalid choice. Try again.")


# Program starts here
main()
