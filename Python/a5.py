import datetime

hand = 40000
checking_account = 40000
savings_account = 9000
log = []

print("#" * 80)
print("#" * 9, " " * 60, "#"*9)
print("#" * 9, "Banking System".center(60), "#" * 9)
print("#" * 9, f"💰 Cash: ${hand}".center(60), "#" * 9)
print("#" * 9, f"💳 Checking Account: ${checking_account}".center(60), "#" * 9)
print("#" * 9, f"💳 Savings Account: ${savings_account}".center(60), "#" * 9)
print("#" * 9, " " * 60, "#"*9)
print("#" * 80)

def main():
    print("1. To Withdraw Money from Checking Account")
    print("2. To Deposit Money to Checking Account")
    print("3. To Withdraw Money from Savings Account")
    print("4. To Deposit Money to Savings Account")
    print("5. View Logs")
    choice = input("Please select the Option (1-5): ")
    if choice == "1":
        withdraw_checking()
    elif choice == "2":
        deposit_checking()
    elif choice == "3":
        withdraw_savings()
    elif choice == "4":
        deposit_savings()
    elif choice == '5':
        view_logs()

def withdraw_checking():
    global hand, checking_account, log
    amount = int(input("How much money do you want to withdraw from checking account? "))
    if amount > checking_account:
        print("Sorry, insufficient funds in checking account!")
        Return()
    else:
        print("Successfully Withdrawn from checking account")
        checking_account -= amount
        hand += amount
        print(f"Updated Hand: ${hand}")
        print(f"Updated Checking Account: ${checking_account}")
        log.append(f"User: Withdrawn ${amount} from Checking Account @ {datetime.datetime.now()}")
        Return()

def deposit_checking():
    global hand, checking_account, log
    amount = int(input("How much money do you want to deposit to checking account? "))
    if amount > hand:
        print("Sorry, insufficient cash amount!")
        Return()
    else:
        print("Successfully Deposited to checking account")
        hand -= amount
        checking_account += amount
        print(f"Updated Hand: ${hand}")
        print(f"Updated Checking Account: ${checking_account}")
        log.append(f"User: Deposited ${amount} to Checking Account @ {datetime.datetime.now()}")
        Return()

def withdraw_savings():
    global savings_account, log
    amount = int(input("How much money do you want to withdraw from savings account? "))
    if amount > savings_account:
        print("Sorry, insufficient funds in savings account!")
        Return()
    else:
        print("Successfully Withdrawn from savings account")
        savings_account -= amount
        hand += amount
        print(f"Updated Hand: ${hand}")
        print(f"Updated Savings Account: ${savings_account}")
        log.append(f"User: Withdrawn ${amount} from Savings Account @ {datetime.datetime.now()}")
        Return()

def deposit_savings():
    global hand, savings_account, log
    amount = int(input("How much money do you want to deposit to savings account? "))
    if amount > hand:
        print("Sorry, insufficient cash amount!")
        Return()
    else:
        print("Successfully Deposited to savings account")
        hand -= amount
        savings_account += amount
        print(f"Updated Hand: ${hand}")
        print(f"Updated Savings Account: ${savings_account}")
        log.append(f"User: Deposited ${amount} to Savings Account @ {datetime.datetime.now()}")
        Return()

def Return():
    choice = input("Want To Do Another Transaction (yes or no)? ")
    if choice.lower() == 'yes':
        main()
    else:
        return

def view_logs():
    global log
    if log:
        for entry in log:
            print(entry)
    else:
        print("No Logs")

if __name__ == "__main__":
    main()
