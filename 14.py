# import csv
# data=[
#     ['Aaa', 10, 'Nepal'],
#     ['Bbb', 20, 'China']
    
# ]
# header=['Name', 'age', 'country']
# with open('output.csv', 'w', newline='') as file:   #newline is default
#     writer=csv.writer(file)
#     writer.writerow(header)
#     writer.writerows(data) #write rows writes the data in bulk

#dictreader and dictwriter   =show the data in the form of dictionary ie key-value pairs
# import csv
# with open('output.csv','r') as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row['Name'])  #if only row- shows all values

# import csv
# data=[
#     {'Name': 'Aaa', 'Age': '10', 'Country': 'Nepal'},
#     {'Name': 'Bbb', 'Age': '20', 'Country': 'China'}
# ]
# headers=['Name','Age','Country']
# with open('dictoutput.csv','w',newline='') as file:
#     writer=csv.DictWriter(file,fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(data)


#json= communication data format=dictionary in python
# import json
# data={'Name': 'Aaa', 'Age': '10', 'Country': 'Nepal'}
# json_data=json.dumps(data)
# # print(json_data)    #outputs the data in the json(string format)
# dict_data=json.loads(json_data)   #converts the json data to dictionary
# print(dict_data)


# import json
# data={'Name': 'Aaa', 'Age': '10', 'Country': 'Nepal'}
# with open('data.json', 'w') as file:
#     json.dump(data,file,indent=4) #indent gives the space and makes it more readable, if not data is written in a single line

# import json
# data={'Name': 'Aaa', 'Age': '10', 'Country': 'Nepal'}
# with open('data.json', 'r') as file:
#     user=json.load(file)   #load is for reading the data as it is
#     print(user)

#banking system in file 