users={
    'Anu':{
        'id':1,
        'username':'Anu',
        'password':'pass'
        #pin
        #balance    in banking system login ans sign ask pin bafore adding and withdrawing the amount
    },
    'Aaa':{
       'id':2,
        'username':'Aaa',
        'password':'password' 
    }
}
def login(username, password):
    user=users.get(username)
    if user:
        if user['password']==password:
            print('login success')
        else:
            print('invalid password')
    else:
        print('user not registered')
login('Aaa','password')

def signup(username,password):
    user=users.get(username)
    if user:
        print('user already available')
    else:
        users[username]={
            'id':len(users)+1,
            'username':username,
            'password':password
        }
signup('Bbb','Ccc')   

print(users)    




