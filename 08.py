#banking system , take pin input if pin match show options- add balance, withdraw, check, exit, take pin input
#give 3 attempts if pin incorrect then exit
pin=12345
#user_pin=int(input('Enter your pin: '))
is_pin_valid=False

for i in range (3):
  user_pin=int(input('Enter your pin: '))
  if pin==user_pin:
    is_pin_valid=True
    break
  print('Invlid pin')
else:
 
 print('out of attempt')


while True:
  if is_pin_valid:

   print('##Welcome to the banking system!')
   print('1. add balance.')
   print('2. Withdraw amount')
   print('3 check balance')
   print('4. Exit')

   choice=input('Enter your choice:')
   if choice=='1':
     bal=0
     add_bal=int(input('Enter the balance you want to add:'))
     bal=bal+add_bal
     print(f'Balance added successfully! New balance: {bal}')

   elif choice=='2':
     withdraw_amt=int(input('Enter the balance you want to withdrow:'))
     if withdraw_amt>bal:
       print('Insuffecient amount!!!')
     else:
       bal=bal-withdraw_amt
       print(f'Amount withdrawn successful. \n Remaining balance: {bal}' )
   elif choice=='3':
     print(f'Your balance amount is: {bal}')
   elif choice=='4':
     print('Thank you!!')
     break
   else:
     print('Enter the choices from 1 to 4')
        
     
      
# elif pin!=user_pin:
#   for i in range 2:
#  print('Incorrect pin, enter the pin') 



 
