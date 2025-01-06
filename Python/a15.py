import datetime

class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.log = []

    def deposit(self, amount):
        self.balance += amount
        self.log_transaction(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.log_transaction(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def log_transaction(self, message):
        self.log.append(f"{message} @ {datetime.datetime.now()}")

    def view_logs(self):
        if self.log:
            for entry in self.log:
                print(entry)
        else:
            print("No Logs")

class CheckingAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

class ATM:
    def __init__(self):
        self.hand = 40000
        self.checking_account = CheckingAccount(40000)
        self.savings_account = SavingsAccount(9000)

    def main_menu(self):
        print("#" * 80)
        print("#" * 9, " " * 60, "#" * 9)
        print("#" * 9, "Banking System".center(60), "#" * 9)
        print("#" * 9, f"💰 Cash: ${self.hand}".center(60), "#" * 9)
        print("#" * 9, f"💳 Checking Account: ${self.checking_account.balance}".center(60), "#" * 9)
        print("#" * 9, f"💳 Savings Account: ${self.savings_account.balance}".center(60), "#" * 9)
        print("#" * 9, " " * 60, "#" * 9)
        print("#" * 80)

        while True:
            print("1. To Withdraw Money from Checking Account")
            print("2. To Deposit Money to Checking Account")
            print("3. To Withdraw Money from Savings Account")
            print("4. To Deposit Money to Savings Account")
            print("5. View Logs")
            print("6. Exit")
            choice = input("Please select the Option (1-6): ")
            if choice == "1":
                self.withdraw_from_checking()
            elif choice == "2":
                self.deposit_to_checking()
            elif choice == "3":
                self.withdraw_from_savings()
            elif choice == "4":
                self.deposit_to_savings()
            elif choice == '5':
                self.view_logs()
            elif choice == '6':
                break

    def withdraw_from_checking(self):
        amount = int(input("How much money do you want to withdraw from checking account? "))
        self.checking_account.withdraw(amount)
        self.hand += amount

    def deposit_to_checking(self):
        amount = int(input("How much money do you want to deposit to checking account? "))
        if amount <= self.hand:
            self.checking_account.deposit(amount)
            self.hand -= amount
        else:
            print("Insufficient cash amount")

    def withdraw_from_savings(self):
        amount = int(input("How much money do you want to withdraw from savings account? "))
        self.savings_account.withdraw(amount)
        self.hand += amount

    def deposit_to_savings(self):
        amount = int(input("How much money do you want to deposit to savings account? "))
        if amount <= self.hand:
            self.savings_account.deposit(amount)
            self.hand -= amount
        else:
            print("Insufficient cash amount")

    def view_logs(self):
        print("Checking Account Logs:")
        self.checking_account.view_logs()
        print("\nSavings Account Logs:")
        self.savings_account.view_logs()

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
