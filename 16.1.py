# in banking class bank acc =accnum and balance ,  3 methods add balance, withdraw_balance(),  show _balance()
#current acc and saving acc,  =classes  , also interest rate,   current acc=overdraft limit withdraw not allowed
#in saving allowed
class BankAccount:
    def __init__(self, accnum, balance):
        self._accnum = accnum
        self.balance = balance
    
    def add_balance(self, amount):
        self.balance += amount
        print(f"Added {amount}. New balance: {self.balance}")

    def withdraw_balance(self, amount):
        pass  # To be overridden in child classes

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

#  Saving Account
# s = SavingAccount("123", 1000, 0.03)
# s.show_balance()
# s.add_balance(500)
# s.withdraw_balance(1300)
# s.withdraw_balance(1500)  # Should be denied

# Current Account 
# c = CurrentAccount("456", 1000, 500)
# c.show_balance()
# c.withdraw_balance(1200)
# c.withdraw_balance(1600)  # Should be denied

print('Welcome to banking system!')
acc_type=input('Enter account type (current/saving): ').strip().lower()
accnum=input('Enter the accuntnumber:')
balance=float(input('Enter the balance'))
if acc_type=="saving":
    interest_rate=float(input('Enter the interest rate :'))
    account = SavingAccount(accnum, balance, interest_rate)

elif acc_type=="current":
    overdraft_limit=float(input('Enter the overdraft limit: '))
    account=CurrentAccount(accnum,balance,overdraft_limit)
else:
    print('invalid account type')
    exit()

while True:
    print("1. Show Balance")
    print("2. Add Balance")
    print("3. Withdraw Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice=='1':
        account.show_balance()
    elif choice=='2':
        amount=float(input('Enter the amount you want to deposit: '))
        account.add_balance(account)
    elif choice=='3':
        amount=float(input('Enter the amount you want to withdraw: '))
        account.withdraw_balance(amount)
    elif choice=='4':
        print('Thankyou!')
        break
    else:
        print('invalid choice please choose between 1-4')


