import pandas as pd

dict = {'name':['sreeni','Raghav','Hari'], 'batch':['b1','b2','b3'], 'age':[30,35,40]}

list = [1,2,3,4]
print(dict)

df = pd.DataFrame(dict)

print(type(df))

print(df)

df2 = pd.DataFrame(list,columns=['sno'],)
#print(help(pd.DataFrame))
print(df2)

df3 = pd.read_csv(r"/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")
print(df3)
print("Top n records")
print(df3.head(2))
print("bottom n records")
print(df3.tail(2))
print("List all the columns")
print(df3.columns)
print("List all the datatype")
print(df3.dtypes)
print("Dataframe rows and column ")
print(df3.shape)
print("Number of rows",df3.shape[0])
print("Number of cols",df3.shape[1])

df4 = pd.read_csv(r"/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")
df5 = pd.read_csv(r"/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info_t.csv")


print("Concat of two DF's without axis")
print(pd.concat([df4, df5])) # Vertical join/union all operation on SQL

print("Concat of two DF's with axis")
print(pd.concat([df4, df5], axis=1)) # Horizontal join

dict1={'cust':['x','y','z','k','r'],'prod_code':[1,2,3,6,7]}
dict2={'cust':['a','z','w','v'],'prod_code':['KA','TN','MH','AP']}
df6=pd.DataFrame(dict1)
df7=pd.DataFrame(dict2)

print("Concat of two DF's without axis")
print(pd.concat([df6, df7])) # Vertical join/union all operation on SQL

print("Concat of two DF's with axis")
print(pd.concat([df6, df7], axis=1)) # Horizontal join

print("Concat of two DF's with axis")
print(pd.concat([df6, df7], axis=1)) # Horizontal join
print("Concat of two DF's with axis=1 and join")
print(pd.concat([df6,df7],axis=1,join='outer'))
print("Merge")
print(df6)
print(df7)
print(pd.merge(df6,df7, on='cust', how='outer'))


df8 = pd.read_csv(r"/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")
print(df8)
#print(df8.Identifier)
#print(df8['Identifier'])
print(df8.loc[3:6,'Identifier':'Phone'])
print(df8.iloc[3:6,0:5])

from pandasql import sqldf

df9 = sqldf('''select count(1), Identifier from df8 group by Identifier
            having count(1)>1''')
print("SQL query")
print(df9)

import pandas as pd
from ydata_profiling import ProfileReport
df8 = pd.read_csv(r"/Users/harish/PycharmProjects/pythonProject/source_files/Contact_info.csv")

profile = ProfileReport(df8)
#print(profile.to_notebook_iframe())
profile.to_html()



