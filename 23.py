#SQL-  sqlite  =.connect method
#database interfare tool ==dbeaver
import sqlite3
connection =sqlite3.connect('mydb.db')
# print(connection)
cruser=connection.cursor()
# query='''
# create table  if not exists users(
# id integer primary key,
# username text not null,
# age int,
# email text unique
# )'''
# cursor.execute(query)

# query='''
# insert into users (username, age, email) values ('aaaa', 50, 'aaa@1gmail.com')
# '''

# data=[
#     ('bbb', 20,'bbb@gmail.com'),
#     ('ccc',33, 'ccc@gmail.com')
# ]
# query='''
# insert into users(username, age, email) values(?,?,?)
# '''
# cruser.executemany(query,data)
# connection.commit()

query='select * from users'   #where id=1
cruser.execute(query)
rows=cruser.fetchall()
print(rows)
# for row in rows:
#     print(row)
connection.commit()
cruser.close()
connection.close()

#store data in database login and signup

