#find the dot product between two vectors v1 and v2
# vector1 = list(map(int, input("Enter elements of first vector separated by space: ").split()))
# vector2 = list(map(int, input("Enter elements of second vector separated by space: ").split()))
# # Check if both vectors have the same length
# if len(vector1) != len(vector2):
#     print("Error: Vectors must be of the same length.")

# Define the vectors
# v1 = [1, 2, 0]
# v2 = [4, 5, 22]
# dot_product = 0
# for i in range(len(v1)):
#     dot_product += v1[i] * v2[i]
# print("Dot product:", dot_product)



users = {}
def sign_up():
    print("\nSign Up")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")

        if username in users:
            raise Exception("Username already exists.")
        
        users[username] = password
        print("Account created successfully!")

    except Exception as e:
        print("Sign up failed:", e)

def login():
    print("\nLogin")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    try:
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")
        
        if username not in users:
            raise Exception("User not found.")
        
        if users[username] != password:
            raise Exception("Invalid password.")
        
        print("Login successful!")
        return True

    except Exception as e:
        print("Login failed:", e)
        return False

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
# Main Program
while True:
    print("\nWelcome to the Bank")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    main_choice = input("Enter your choice (1-3): ")

    if choice == '1':
        sign_up()

    elif choice == '2':
        if login():
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
                continue

            while True:
                print("\n1. Show Balance")
                print("2. Add Balance")
                print("3. Withdraw Balance")
                print("4. Logout")
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
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice! Please enter 1-4.")

    elif choice == '3':
        print("Thank you!")
        break

    else:
        print("Invalid input! Please enter 1,2 or 3")

