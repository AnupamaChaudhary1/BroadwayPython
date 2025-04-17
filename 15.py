#oop 
#__init()__special method ,   self-keyword represents the instance of class,  
# class User:
#     def login(self):   # function inside the class is considered method
#         print('User logged in')
#     def signup(self):
#         print('User signed up')
# user1=User()   #creatiing object 
# user1.login()
# user1.signup()


#constructor== when called automatically invokes the fxn  method, defines class properties,  
class User:    
    nationality='Nepali'  #class variable
    def __init__(self,username, password):  #argument
        self.username=username   #object variable or attribute
        self.password=password
    def login(self):
        print(f'User {self.username} logged in')
    def signup(self):
        print(f'User {self.username} signed up')
user1=User('Aaa','password')   #creatiing object , list of arguments ,   --object attribute
user1.login()
user1.signup()
print(User.nationality)  #directly accessible to class variable or
print(user1.nationality)

