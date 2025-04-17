class User:
    def __init__(self): 
      self.users={}
    def login(self,username, password):
       user = self.users.get(username)
       if user:
        if user['password'] == password:
            print(f'Login success! Welcome {username}')
            return user
        else:
            print('Invalid password')
       else:
        print('User not registered')  
    def signup(self,username, password, pin):
      user=self.users.get(username)
      if user:
        print('User already exists!')
      else:
        self.users[username] = {
            'id': len(self.users) + 1,
            'username': username,
            'password': password,
            'pin': pin,
            'balance': 0
        }
        print(f'User {username} registered successfully.')
        return self.users[username]
user = User()
user.signup('John', 'password', 1234)
user.login('John','password123')



     
    