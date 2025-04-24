#visualization-  conversion in graph,  matplotlib(customizable) and seaborn(simplifies statistical ) datavisualization libraries
# 
# import matplotlib.pyplot as plt
# x=[1,2,3,5,6]
# y=[6,21,12,5,14]
# plt.plot(x,y, color='green')
# plt.title('Line graph')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.show()

# categories=['A','B','C']
# values=[4,5,2]
# plt.bar(categories,values,color='black')
# plt.title('Bar graph')
# plt.xlabel('Values')
# plt.ylabel('Categories')
# plt.show()

# sizes=[50,30,10,10]
# labels=['a','b','c','d']
# plt.pie(sizes,labels=labels, autopct='%1.1f%%')
# plt.title('Pie Chart')
# plt.show()

#numpy =work with array
#Seaborn= better for statistical plots,    simplified and builtin type
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=np.random.rand(6,5)    #5 is for columns and 6 is range/rows
df=pd.DataFrame(data, columns= ['A','B','C','D','E'])
sns.heatmap(df)  #,cmap='coolwarm'
plt.show()

#boxplot 
#pairplot =using seaborn



