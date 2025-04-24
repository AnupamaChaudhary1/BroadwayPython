#built in modules -os=file name (operating system)
#getcwd(current work directory)=gives the location in which we are working
#os.mkdir('') ,rmdir=remove

# import os
# print(os.getcwd())
# os.remove('test.txt')
# os.mkdir('test')              #os docs
# os.rmdir('test')


# random module=to generate random numbers
# import random
# colors=['red','yellow','white']
# print(random.choice(colors))
# random.shuffle(colors)
# print(colors)
# print(random.randint(1,9))
# print(random.randrange(100,999))



# import random

# for i in range(5):
#     x=int(input('enter the number between 1 to 50 of your choice: '))
#     if x==random.randint(1,50):
#       print('the number matched')
#       break
#     elif x>random.randint(1,50):
#        print('incorrect')
#        print(f'number of attempts left: {5-i}')
    
#     elif x<random.randint(1,50):
#        print('incorrect')
#        print(f'number of attempts left: {5-i}')
# else:
#    print(f'Numbers do not match. out of attempt. correct is:{random.randint(1,50):}')
         
    
#math for different methods
# import math
# num=5.63
# print(math.floor(num))  #lower value
# print(math.ceil(num))   #upper value for decimal numbers



#user declared module
#we cam also import the built in function =module function, varialble , list files /....
# from calc import sum, diff,var   #imported form calc.py
# print(var)
# print(sum(3,5))
# print(diff(6,3))


# 3rd party modules like pandas(pip helps to install=pip install pandas in system)
# python -m venv venv(name any name given by us),


#random number algorithms 
def simple_lcg(seed):
    a = 9
    c = 3
    m = 2**3
    seed = (a * seed + c) % m
    return seed

seed = 4  # Initial seed

for i in range(1,3):
    x=int(input('enter the number between 1 to 10 of your choice: '))
    seed = simple_lcg(seed)
    random_int = 1 + (seed % 10)  # Random integer in [1, 10]
    if x==random_int:  #[1,10]:
      print('the number matched')
      break
    elif x>random_int:  #[1,10]:
       print('incorrect')
       print(f'number of attempts left: {3-i}')
    
    elif x<random_int:  #[1,10]:
       print('incorrect')
       print(f'number of attempts left: {3-i}')
else:
   print('Numbers do not match. out of attempt!')
   
print("Correct is Random Integer:", random_int)










