# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __mul__(self,other):
#         return self.x*other.x + self.y*other.y
# v1=Vector(1,2)
# v2=Vector(4,5)
# print(v1*v2)


#lamda function anynomus function=lamda function , used when we have to pass any small function inside the main function
#one line function
# sum=lambda a,b: a+b
# result=sum(1,4)
# print(result)


#iterator and generator
#iterable=numbers where we apply loop
#iterator:  through which we iterate (the object) =(iter and next)
# numbers=[2,4,5,7,9]
# # i_numbers=numbers.__i()
# i_numbers=iter(numbers)
# for num in i_numbers:
#     print(num)
# print(next(i_numbers))


# class MyRange:
#     def __init__(self,start,end):
#         self.value=start
#         self.end=end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value>=self.end:   #checking the condition and stop the loop to satisfy the conditons.
#             raise StopIteration
        
#         current=self.value
#         self.value+=1    #any condition
#         return current
# myrange=MyRange(1,7)
# for i in myrange:
#     print(i)


#generator =special function to return iterator
#generator only occupy the  memory forcurrent value only=memory efficient
# def my_range(start,end):
#     current=start
#     while current<end:
#         yield current     #in generator yield is used- it help to continue the loop without break
#         current+=1
# myrange=my_range(3,8)
# for i in myrange:
#     print(i)


# is =identity operator -checks if two are in same memory location or not
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# print(id(a))
# print(id(b))

# a=[1,2,4]
# b=a
# a[0]=1
# print(a)
# print(b)


#decorator = tool used to decorate the function, helps in adding certaion functionlaity without changing the original
# def handle_error(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print(f'error while callin function {func.__name__}:',e)
#     return wrapper
# @handle_error
# def divide(a,b):
#     return a/b
# @handle_error
# def sum(a,b):
#     return a+b
# divide(1,0)
# sum(1,'4')


