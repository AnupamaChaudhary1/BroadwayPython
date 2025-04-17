users=[
    {
        'id':1,
        'username':'Anu',
        'password':'pass'
    },
    {
       'id':2,
        'username':'Aaa',
        'password':'password' 
    }
]
def login(username, password):
    for user in users:
        if user['username']==username:
            if user['password']==password:
               print('Login successful!')
               break
            else:
               print("invalid password")
               break
    else:                                 #to run the condition outside the loop to check username
        print('invalid username')
login('Aaa','password')
#to signup to check if it is already is in, if not then store in sets
def signup(username, password):
    for user in users:
        if user['username']==username:
            print('username already available, use different name')
            break
    else:
        users.append({
            'id':len(users)+1,
            'username':username,
            'password':password
        })
        print('user registered')
    
signup('Bbb','Ccc')
print(users)

#or use flags
# def signup(username, password):
#     user_found=False
#     for user in users:
#         if user['username']==username:
#             user_found=True
#             break
#         if user_found:
#             print('already found')
#     else:
#         print('Signup successful')
#         users.append({
#             'id':len(users)+1,
#             'username':username,
#             'password':password
#         })
#         print('user registered')
    
# signup('Bbb','Ccc')
# print(users)