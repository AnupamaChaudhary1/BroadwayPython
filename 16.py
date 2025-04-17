#Encapsulation== Encapsulation may also refer to containing a repetitive or complex process in a single 
# unit to be invoked. Object-oriented programming facilitate this at both the method and class levels. 
# This definition is also applicable to procedural programming.   
# class BankAccount:
#     def __init__(self, accnum, balance):  #__ for private (access accessifier, and nothing for public)
#         self.__accnum=accnum
#         self.__balance=balance
#     def get__accnum(self):  #getter
#         print(self.__accnum)
    
# acc1=BankAccount(201,200)
# acc1.get__accnum()

# class Animal:
#     def speak(self):
#         print('Animal speaks')

# class Dog(Animal):    # single inheritance
#     def bark(self):
#         print('Dog barks')
# dog=Dog()
# dog.bark()
# dog.speak()


#multiple inheritancce left is given more priority,  MRO=method resolution order
# class Animal:
#     def speak(self):
#         print('Animal speaks')
#     def eat(self):
#         print('Animal eats')
# class Mammal:
#     def eat(self):
#         print('Mammal eats')
# # class Dog(Animal,Mammal):    
# #     def bark(self):
# #         print('Dog barks')
# class Dog(Mammal,Animal):    #  inheritancce left is given more priority,  MRO=method resolution order
#     def bark(self):
#         print('Dog barks')
# d=Dog()
# d.speak()
# d.eat()
# d.bark()


#multilevel inheritance= 
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        print(f'Area of length {self.length} and breadth {self.breadth} = {self.length*self.breadth}')
class Square(Rectangle):
    def __init__(self, l):
        super().__init__(l,l)
sqr=Square(10)
sqr.area()
        

# in banking class bank acc =accnum and balance ,  3 methods add balance, withdraw_balance(),  show _balance()
#current acc and saving acc,  =classes  , also interest rate,   current acc=overdraft limit withdraw not allowed
#in saving allowed


