# is_person=True
# is_valid=False
# print(is_person and is_valid)
# print(is_person or is_valid)
# print(not is_person)

# age=12
# if age>=18:
#     print("The person can vote")
# elif age<=0:
#   print("invalid age")
# else:
#     print("He cannot vote")

# profit and loss
# CP=float(input("Enter the Cost Price:"))
# SP=float(input("Enter the selling price:"))
# if SP>CP:
#     print("It is profit, Profit=",SP-CP)
# elif CP>SP:
#     print("It is loss,loss is=",CP-SP)
# else:
#     print("SP and CP are equql")
# # profit= SP-CP
# print("the profit is:",profit)

#income tax is a person is married or unmarried
#married -  income>100000 tax=10% or 8% tax
#unmarried -income>100000 tax=12% or tax=10%

# Status= input("Enter the status of a person:")
# Income=int(input("Enter the income of a person:"))
# if Status.lower()=='m':
#   if Income>100000:
#     tax=Income*0.1
#     print("Tax:",tax)
#   else:
#     tax=Income*0.08
#     print(tax)
# elif Status=='U':
#   if Income>100000:
#     tax=Income*0.12
#     print("Tax:",tax)
#   else:
#     tax=Income*0.1
#     print(tax)
# else:
#   print("Invalid Status!")

# 1.fizz, buzz or fizzbuzz divide by 3,5, and both if not then print the number
# 2.greater among three numbers
# x=int(input("Enter the number:"))
# if x % 3==0 and x % 5!=0:
#   print("It is fizz")

# elif x % 5==0 and x % 3 !=0:
#   print("It is buzz")
# elif x % 3==0 and x % 5==0:
#   print("It is fizzbuzz")
# else:
#   print(x)

# x=int(input("Enter first number:"))
# y=int(input("Enter second number:"))
# z=int(input("Enter third number:"))
# if x>y and x>z:
#   print(f"{x} is greatest")
# elif y>x and y>z:
#   print(f"{y} is greatest")
# else:
#   print(f"{z} is greatest.")

name="AAA"
address="bbb"
print("my name is " + name + " my address is " + address) #concat
print("My name is {} and My address is {}".format(name, address)) #formatting
print(f"My name is {name} and My address is {address}") #f-string
