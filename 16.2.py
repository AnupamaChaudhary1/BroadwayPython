class BankAccount:
    def __init__(self, accnum, balance):
        self._accnum = accnum
        self.balance = balance
    
    def add_balance(self, amount):
        self.balance += amount
        print(f"Added {amount}. New balance: {self.balance}")

    def withdraw_balance(self, amount):
        pass  # To be overridden

    def show_balance(self):
        print(f"Account Number: {self._accnum}, Balance: {self.balance}")


class SavingAccount(BankAccount):
    def __init__(self, accnum, balance, interest_rate):
        super().__init__(accnum, balance)
        self.interest_rate = interest_rate
        

    def withdraw_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Withdrawal denied! Insufficient balance.")


class CurrentAccount(BankAccount):
    def __init__(self, accnum, balance, overdraft_limit):
        super().__init__(accnum, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_balance(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal denied! Overdraft limit exceeded.")


# ----------------------------
# User Input Section
# ----------------------------

print("Welcome to the Bank!")
acc_type = input("Enter account type (saving/current): ").strip().lower()

accnum = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

if acc_type == "saving":
    interest_rate = float(input("Enter interest rate (e.g., 0.03 for 3%): "))
    account = SavingAccount(accnum, balance, interest_rate)

elif acc_type == "current":
    overdraft_limit = float(input("Enter overdraft limit: "))
    account = CurrentAccount(accnum, balance, overdraft_limit)

else:
    print("Invalid account type!")
    exit()

while True:
    print("1. Show Balance")
    print("2. Add Balance")
    print("3. Withdraw Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        account.show_balance()

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        account.add_balance(amount)

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw_balance(amount)

    elif choice == '4':
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
