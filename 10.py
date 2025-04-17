#Dictionary =collection of data in key value pair
# thidict={
#     'name':'aa',
#     'address':'nepal',
#     'age' : 90
# }
# thidict['place']='aaaaa'
# thidict['age']=60
# print(thidict.get('name'))
# print(thidict.pop('age')) #pop and also show the removed item
# del thidict['address'] #remove
##thidict.popitem()  #it removes the last item
# print(thidict)

#.keys, .values(), .items()=item and values both,   len(),  clear()=clears dictionary  

# user={
#     'name':'aa',
#     'address':'nepal',
#     
# }
# print(type(user.keys()))
# print(user.values())
# print(user.items())
# print(user.clear())

 #loop in dictionary  
# for key in user:  #returns keys only
#     print(key)

# for value in user.values():  # returns values only
#     print(value)

# for key, value in user.items(): #retruns key and values both
#     print(f'{key}==={value}')

#nested dictionaries 
# user={
#     'name':'aa',
#     'address':{
#        'province':'Bagmati',
#        'district':'lalitpur'
#     }
# }
# user['address']['province']='Province 3' # for changing
# print(user['address']['province'])

#dictionary comprenhsion = 
# words=['apple', 'banana', 'cherry'] #find the length
# print({word:len(word) for word in words }) #or

# word_len={}
# for word in words:
#     word_len[word]=len(word)
# print(word_len)

# nested
users = [
    {
        'name':'aaa',
        'password':'pppp'
    },

    {
        'name':'aaa',
        'password':'pppp'
    }
]
print(users[0]['name'])



