#data manipulation tool,  dataformats- series(1D) and dataframe(2D)=can be thought as sql table or spreadsheet
import pandas as pd
data={
    'Name': ['Aaa','Bbb','Ccc'],
    'Age': [1,90,3],
    'City': ['Ktm','Pokhara','Ddd']
}
# data=[
#     ['Aaa',100,'OOO']
# ]
# data = [
#     {'Name': 'Bob', 'Age': 20, 'City': 'Chicago'},
#     {'Name': 'Mohit', 'Age': 20, 'City': 'Kapilvastu'}
# ]
df=pd.DataFrame(data)

#.head() and .tail   if no argument passed first and last 5 rows is shown
# print(df.head(2))
# df=pd.DataFrame(data,columns=['Name','Age','City'])
# print(df)

# multiple frames
# print(df['Name'])
# print(df[['Name', 'City']])        # to select the specific data 

# To filter the data
# filter_df=df[df['Age']>2]         
# print(filter_df)

# df['IsAdult']=df['Age']>2
# print(df)

df.drop(columns=['Name'], inplace=True)
# print(df.sort_values(by='Age', ascending=False))
print(df.groupby('City').mean())
# print(df)
 

# df = pd.read_csv('data.csv')
# print(df)
df.to_csv('pdoutput.csv', index=False)

#mediamn mode---, drop on the basis of col...and so on....


