#Function= reusable block of code designed to perform specific task
#def func_name(parameters):   return expression,     only one return statement,  
# default value(in last) in argument if value is not provided 
#global valiable(declared outside function)=accessibel outside function and inside also and local variable =only accessible inside the function
# use global x(var) to make it global
#args and **kwargs= disctonary form, *args=tuples [for infinite arguments]

# def sum(n1, n2):
#     sum=n1+n2
#     return sum
# result1=sum(1,4)
# result2=sum(6,7)
# print(result1)
# print(result2)

# def get_stats(numbers):
#     max_value=max(numbers)
#     min_value=min(numbers)
#     sum_value=sum(numbers)
#     return max_value,min_value,sum_value
# numbers=[1,3,6,8,4,7,9,0]
# max_val,min_val,total_val=get_stats(numbers)   #tuple unpacking
# print(max_val)
# print(min_val)
# print(total_val)

# values=get_stats(numbers) #in the form of tuples
# print(values)

#in dictionary format
# def get_stats(numbers):
#     max_value=max(numbers)
#     min_value=min(numbers)
#     sum_value=sum(numbers)
#     return{
#         'max_value':max_value,
#         'min_value':min_value,
#         'sum_value':sum_value
#     } 
          

# numbers=[1,3,6,8,4,7,9,0]
# result=get_stats(numbers)
# print(result['max_value'])

#deault values
# def calculate_total(unit_price, qun=1, dis=0.2):
#     '''
#     description: calculates total price based on qun and disc
#     paramaters:
#        :unit_price-> int
#        :uqun-> int
#        :dis-> float
#     returns:
#     '''
#     price=unit_price*qun*dis
#     total_price=price-dis+price
#     print(f'The total price is: {total_price}')
# print(calculate_total.__doc__)
#  calculate_total(90000,5,6)
#  calculate_total(200)



# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




# def sum_nums(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
# # Example usage:
# print(sum_nums(1, 2, 3, a=4, b=5))  # Output: 15


#calulate the sum of infinite numbers passed to a function.   using *args and **kwarks
def sum_nums(*numbers):
    return sum(numbers)
print(sum_nums(2,6,8,3.5,8,9,0,3,5,7,9,6))
print(sum_nums(2,1))


