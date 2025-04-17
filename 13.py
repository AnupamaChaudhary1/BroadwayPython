#file handling
#write removes prevous but append adds new contents
#read, write, remove modes
#f.readline()= shows single line,    readlines in list,   
# f=open('test.txt', 'r')
# print(f.read())
# print(f.readline()) #gives space between two lines as we entered in text files
# print(f.readline())
# print(f.readlines())
# prints the first 7 letters of the text


#  #if not closed memory may be leaked and cause issues, 

# with open('test.txt','r') as file:      #context manager: for memory management
#     for line in file:
#         print(line.strip())

# with open('test2.txt','a') as file:    #a adds new conntents to existing
#     file.write('\nThis line is added')

# data=["line 1\n", "line 2"]    #to add data in bulk
# with open('test2.txt','w') as file:
#     file.writelines(data)

# 'x' mode      
# data = ["line 1\n", "line 2\n"]
# with open('test3.txt', 'x') as file:
#     file.writelines(data)

# import os    #delete the existing file
# os.remove("test3.txt")

#csv=comma seperated values,   header and actual values,  tsv =tab, psv=pipe
# import csv
# with open('data.csv') as file:
#     reader= csv.reader(file)
#     for line in reader:
#         print(line)


