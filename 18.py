# Exception handling
# class Book:
#     def __init__(self,name,pages):
#         self.name=name
#         self.pages=pages
#     def __eq__(self,other):
#         return self.name==other.name and self.pages==other.pages
# b1=Book('A', 1000)
# b2=Book('A',1000)
# print(b1==b2)
        

#exception Handling =unexpected error
#syntax error and semantic error(logical error)
#try, except and finally in python else also
# def divide(num1,num2):
#     try:
#        result=num1/num2
#        print(result)
#     except ZeroDivisionError as e:
#         print('cannot divide a number by 0 so default divided by 2')
#         result=num1/2
#         print(result)
#     except TypeError as e:
#         print('Type error occured: ',e)
#     except Exception as e:
#         print('Error occuredL: ',e)
#     else:  #if try successfully executed then goes to else block
#         print('inside else')

#     finally:
#         print('Exception completed..')
# divide(1,3)
# divide(6,0)
# divide(6,'3')


# class ValidationError(Exception):
#     def __init__(self, message,code):
#         super().__init__(message)
#         self.code=code
    
# def divide(x,y):
#     if y==0:
#         raise ValidationError('Cannot divide a number by 0',400)
#     else:
#         print(x/y)
# try:
#     divide(1,0)
# except ValidationError as e:
#     print('Error occured:',e)
#     print(e.code)
