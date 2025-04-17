#Looping
# for i in range(1,11):
#     print("Python")

#sum of first 20 numbers
# sum=0
# for i in range(1,21):
#     sum=sum+i
# print(sum)

#factorial of number
# fact=1
# n=int(input("enter the number:"))
# for i in range (1,n+1):
#   fact=fact*i
# print(fact)

# fact=1
# n=int(input("enter the number:"))
# while n>0:
#   fact=fact*n
#   n=n-1
# print(fact)

#palindrome if number is revrsed then same output eg 121 and 121
# num = int(input("Enter a number: "))
# if str(num) == str(num)[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


num = int(input("Enter a number: ")) 
original = num  
reverse = 0 
while num > 0: 
    digit = num % 10  
    reverse = reverse * 10 + digit 
    num //= 10  

# Compare the original number with the reversed number
if original == reverse:
    print("Palindrome")  
else:
    print("Not a palindrome") 
