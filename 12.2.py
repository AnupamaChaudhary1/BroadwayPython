# users = {
#     'Anu': {
#         'id': 1,
#         'username': 'Anu',
#         'password': 'pass',
#         'pin': '1234',
#         'balance': 1000
#     },
#     'Aaa': {
#         'id': 2,
#         'username': 'Aaa',
#         'password': 'password',
#         'pin': '4321',
#         'balance': 500
#     }
# }

# def login(username, password):
#     user = users.get(username)
#     if user:
#         if user['password'] == password:
#             print(f'Login success! Welcome {username}')
#             return True
#         else:
#             print('Invalid password')
#             return False
#     else:
#         print('User not registered')
#         return False

# def signup(username, password, pin):
#     if users.get(username):
#         print('User already exists!')
#     else:
#         users[username] = {
#             'id': len(users) + 1,
#             'username': username,
#             'password': password,
#             'pin': pin,
#             'balance': 0
#         }
#         print(f'User {username} registered successfully.')
#         return users[username]
#     return None
# def verify_pin(username, entered_pin):
#     user = users.get(username)
#     if user['pin'] == entered_pin:
#         return True
#     else:
#         return False

# def deposit(username, pin, amount):
#     if verify_pin(username, pin):
#         users[username]['balance'] += amount
#         print(f'{amount} Deposit successful! New balance: {users[username]["balance"]}')
#     else:
#         print('Incorrect PIN')

# def withdraw(username, pin, amount):
#     if verify_pin(username, pin):
#         if users[username]['balance'] >= amount:
#             users[username]['balance'] -= amount
#             print(f'{amount} Withdrawal successful! Remaining balance: {users[username]["balance"]}')
#         else:
#             print('Insufficient balance')
#     else:
#         print('Incorrect PIN')

# # login('Aaa', 'password')
# signup('Bbb', 'Ccc', '1111')
# deposit('Anu', '1234', 2000)
# # withdraw('Aaa', '4321', 500)

# # print(users)

users = {
    'Anu': {
        'id': 1,
        'username': 'Anu',
        'password': 'pass',
        'pin': '1234',
        'balance': 1000
    },
    'Aaa': {
        'id': 2,
        'username': 'Aaa',
        'password': 'password',
        'pin': '4321',
        'balance': 500
    }
}

def login(username, password):
    user = users.get(username)
    if user:
        if user['password'] == password:
            print(f'Login success! Welcome {username}')
            return user
        else:
            print('Invalid password')
    else:
        print('User not registered')
    

def signup(username, password, pin):
    if users.get(username):
        print('User already exists!')
    else:
        users[username] = {
            'id': len(users) + 1,
            'username': username,
            'password': password,
            'pin': pin,
            'balance': 0
        }
        print(f'User {username} registered successfully.')
        return users[username]
    

# ==== Login or Signup loop ====
user = None

while True:
    print("\n==== Welcome to SimpleBank ====")
    print("1. Login")
    print("2. Signup")
    choice = input("Choose an option: ")

    if choice == '1':
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        if login(uname, pwd):
            user = uname
            break
    elif choice == '2':
        uname = input("Choose a username: ")
        pwd = input("Choose a password: ")
        pin = input("Set a 4-digit PIN: ")
        if signup(uname, pwd, pin):
            user = uname
            break
    else:
        print("Invalid option. Try again.")

# ==== Main menu after login/signup ====
while True:
    print(f"\n--- Welcome, {user}!")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("5. show")
    option = input("Choose an option: ")

    if option == '1':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == users[user]['pin']:
            amount = float(input("Enter amount to deposit: "))
            users[user]['balance'] += amount
            print(f"Deposit successful! New balance: {users[user]['balance']}")
        else:
            print("Incorrect PIN")

    elif option == '2':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == users[user]['pin']:
            amount = float(input("Enter amount to withdraw: "))
            if users[user]['balance'] >= amount:
                users[user]['balance'] -= amount
                print(f"Withdrawal successful! Remaining balance: {users[user]['balance']}")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect PIN")

    elif option == '3':
        print(f"Your current balance is: {users[user]['balance']}")
    
    elif option == '5':
        print("\n--- All Users Data ---")
        for user in users.values():
            print(f"ID: {user['id']}, Username: {user['username']}, Balance: {user['balance']}, PIN: {user['pin']}")


    elif option == '4':
        print("Exited.")
        break

    else:
        print("Invalid option. Try again.")

        