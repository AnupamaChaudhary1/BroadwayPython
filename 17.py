#abstraction =data hiding techniques in oop,  help define certain layout in child class
# from abc import ABC, abstractmethod
# class Account(ABC):
#     def __init__(self,accnum, balance):
#         super().__init__()
#         self.accnum=accnum
#         self.balance=balance

#     @abstractmethod
#     def get_acc_details(self):
#         pass

#     def add_balance(self, amt):
#         self.balance+=amt
#         print(f'Rs. {amt} deposited')
# class SavingAccount(Account):
#     def __init__(self, accnum,balance,interest=0.1):
#         super(). __init__(accnum, balance)
#         self.interest=interest
#     def get_acc_details(self):
#         print(f'Amount: Saving\nAcc No; {self.accnum}')


# class CurrentAccount(Account):
#     def __init__(self,accnum, balance, limit=5000):
#         super().__init__(accnum,balance)
#         self.limit=limit
    
#     def get_acc_details(self):
#         print(f'Amount: Current\nAcc No; {self.accnum}')

# s=SavingAccount(111,1000,0.11)
# c=CurrentAccount(1020,40000,4000)
# s.get_acc_details()
# c.get_acc_details()


#polymorphism
#operator overloading-  same operator implemented in multiple places
# class Vector:
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):   #for subtraction use __sub__
#         return Vector(self.x+other.x,self.y+other.y)
#     def __str__(self,):
#         return f'({self.x},{self.y})'
# v1=Vector(2,5)
# v2=Vector(5,9)
# print(v1+v2)  
# print(1+3)    #operator ovrloading
#overloading is the ability to create multiple functions of the same name with different implementations.
#  Calls to an overloaded function will run a specific implementation of that function appropriate to the 
# context of the call, allowing one function call to perform different tasks depending on context


#book class=name and number of pages,  if 2 pages check if pages of book same or not page number equal
class Book:
    def __init__(self,name, pages):
        self.name=name
        self.pages=pages
    def __eq__(self, others):
        if isinstance(others,Book):
            return self.pages==others.pages
    def __str__(self,):
         return f'{self.name} has {self.pages} pages'
book1=Book('English', 300)
book2=Book('C',300)
book3=Book('Java',350)
print(book1)
print(book2)
print(book3)
print(book1==book2)
print(book2==book3)
        
        