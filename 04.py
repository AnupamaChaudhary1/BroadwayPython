#find the length of number using while loop
# num = int(input("Enter a number: "))
# count = 0
# n = abs(num)  # Handle negative numbers

# while n > 0:
#     n //= 10  # Remove the last digit
#     count += 1
# print("Length of the number:", count)

#find the multiplication table of a number for loop
# num = int(input("Enter a number: "))

# for i in range(1, 11):  # Loop from 1 to 10
#     print(f"{num} × {i} = {num * i}")


#find the multiplication between two numbers for loop
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# for i in range(1, 2):  # Loop runs only once
#     result = num1 * num2  

# print("Multiplication result:", result)


#to check if the number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime")


