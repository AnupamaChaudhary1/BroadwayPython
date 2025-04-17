# string="abcd"
# rev=''
# for i in range(len(string)-1,-1,-1):
#     rev=rev+string[i]
# if rev==string:
#     print("palindrome")
# else:
#     print("not palimdrome")

#list   -append, remove
# numbers=[3,4,6,8,8,1]
# animals=['cat','dog','elephant','cow']
# mixed_list=[1,'apple',True,3.4]
# print(numbers[2:])
# print(animals[:4])
# print(mixed_list[1::2])
# animals[1]='crow'
# animals.append('ten')
# print(animals)
# animals.remove('ten')
# print(animals)
# numbers.insert(1,'num')
# print(numbers)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"] #put watermelon in 2and 3position
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# fruits=['apple','banana','orange','mango']
# for i,fruits in enumerate(fruits,start=1): #i is given to give the index number to the fruit items
#     print(f"{i}. {fruits}") #  for both in
#     #print(fruits) # it dont place in the same line

#list of lists
# a=[
#     [2,3,4,7], #0 with element index 0 1 2 3
#     [4,7,8,9], #1
#     [9,7,6,0]  #2
# ]
# print(a[1])
# print(a[:2])
# print(a[1][2]) #list with number 1 and give the 3rd element ie 0,1,2,3
# sum=0
# for row in a:
#     for col in row:
#         sum=sum+col
#         print(col, end=" ")
#     print("\n")
# print("sum:",sum)

# sum=sum(sum(row)for row in a)
# print("sum:", sum)
# calculate the sum of elements of all the matrix

#membership operators - in,not in for eg used in checking for validation of usernames for login
# fruits=['apple','banana']
# print('orange' not in fruits) #true is not found, false if found
# a=[1,3,5,7,8]
# print(2 in a) # true if found and false if not found


# in list if duplicate elements found remove duplicate and create new list
# list = [1, 2, 2, 3, 4, 4, 5]
# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)  # Output: [1, 2, 3, 4, 5]

#Tuple immutable
#insert= to add at any position, pop(1)=position, sort=sorted(numbers), extend=used to combine new list to previous, append, remove('apple')
# n1=[1,2,5,7,9]
# n2=[3,8,0,4,8]
# # n1.append(0)
# # n2.remove(0)
# # n1.extend(n2)
# # n1.sort()
# # n1.pop(4) #remove the forth item form the list
# n1.insert(1,100)
# n1.sort(reverse=True)
# print(n1)
# print(n2)


# sq=[]
# for i in range(1,5):
#     sq.append(i**2)
# print(sq)
#list comprehension =create new list from the existing ones, in one line
# sq=[i**2 for i in range(1,9) if i%2!=0]      #[expression  for if condition]
# print(sq)

# products=['EL-123','SS-123','EL-356','ST-390'] # create new list with EL in the list
# new=[i for i in products if "EL" in i] # i.startswith('EL-')
# print([product for product in products if product.startswith('EL-')])
# print(new)

#1. even numbers from the list using list comprehension 
num=[1,2,3,4,5,6,7,8]
print([nums for nums in num if nums % 2 == 0])
#2. write odd and even in place of numbers
print(['Even' if nums %2==0 else 'Odd' for nums in num])


