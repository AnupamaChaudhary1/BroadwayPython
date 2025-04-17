#strings -immutable in python, all datatypes immutable
#single line and double line(triple quotation-multiline comments or docs """)
#starting index starts with 0, strings are sequence of characters
# negative indexing starts from backward ie -1....., 
# slicing create new string from proportions of original, 

# s="Hello, World!"
# print(s[4])
# print(s[7:])
# print(s[:5])
# print(s[-4])
# print(s[::4]) #escape and give every characher after escape give 4th 
# print(s[7::2])
# print(s[::-4]) #reverse
# print(s[3:6])
# print(s[7::-2]) #backward
# print(s[::-1])

#strip removes white space before and after  --lstrip(),rstrip()
# print(s.strip(!)) #removes ! or if nothing removes space only
#len() give the length of the string
# print(len(s))
# s="Hello, World!"
# for i in range(len(s)):
#     print(s[i])

# for char in s:
#     print(char)
          
# for char in s:
#     print(char, end="") #any thing we put in end is displayed between the characters

# print(s.upper())
# print(s.lower())

#continue and break
#substrig =extract certain portion from string
#.replace():, .lower(), .title()=first character upper case
# print(s.replace("World", "Python"))
# print(s.title())
#print(s.split(","))

# join():
# words = ["Hello", "World", "Python"]
# result = " ".join(words) #anything in double quotation marks, if no space then removes space
# print(result)  # Output: Hello world Python

#isdigit(), isupper(), .format()    #checks the condition and gives true of false
# print(s.isdigit())
# print(s.isalpha())
# print(s.istitle())

# fname="Aaa"
# lname="Bbb"
# print(f"My name is {fname} {lname}") #or  print("my name is {} {}" .format(fname, lname))

#paldrome string check
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome string")
else: 
    print("Not a palindrome string")
