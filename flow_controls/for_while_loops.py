'''This file created to practice iterative statements
Author - Sreeni added date:20/Dec/2023 '''

ls = [4,5,6,'Sreeni', True]
t = (44,55,77,'Raghav', False)
d = {1:"Sreeni", 2:"Raghav", 3 :"Mahesh"}
s= {7,1,2,3,4,5,5,6,6}
fs = frozenset({1,4,5,6,7,7,7,8})
r = range(1,10)
#df, series, arrays

#Syntax for

# for value in iterativedata:
#     statement1
#     statement2

print("The list ls is ",ls)
print("first value ",ls[0])
print("second value ",ls[1])
print("third value ",ls[2])
print("fourth ",ls[3])
print("fifth ",ls[4])
print("*"*40)

for i in ls:
    ind = ls.index(i)
    print(f"The value of {i} present in index {ind}")

print("*"*50)
for value in t:
    ind = t.index(value)
    print(f"In Tuple {t}, The value of {value} present in index {ind}")

table  = ['profile', "email", "phone", "transaction"]

for tn in table:
    col = 'id'
    print(f"select id, count(1) from {tn} group by {col} having count(1)>1")

print("The keys present in d",d.keys())
print("The values present in d",d.values())
print("The items present in d ",d.items())

for key, value in d.items():
    print(f"Dictionary {d}, The key is {key} and value is {value}")

print("The set ",s)



for value in s:
    print(f"In set {s}, The value of {value} ")


for i in range(1,11):
    print(i)

print("*"*40)
for i in range(1,11):
    if i % 2 == 1 :
        print(i)

for i in range(1,11):
    for j in range(1,11):
        print("i*j",i,j,i*j)



ls=[1,2,3,'Chiru']
print(dir(ls))
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
t=(1,2,3,'Chiru')
print(dir(t))
#'count', 'index'

ls.append('today')
print(f"the list after appended looks like {ls}")
print(f"the number of times the value today has appeared is :{ls.count('today')}")

ls.reverse()
print(ls)

ls2=[420,'California']

ls.extend(ls2)
print(ls)

#therefore it said that a list is mutable and tuple is immutable
print(dir(d))
#'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

ls=['Bengaluru','Hyderabad','Chennai','Thiruvanathapuram']
for i in ls:
    index=ls.index(i)
    print(i)
    print(index)
    print(f"the city {i} belongs to index {index} in the above list")


print("*"*50)
for value in t:
    ind = t.index(value)
    print(f"In Tuple {t}, The value of {value} present in index {ind}")



print("*"*50)
dict={"States":["Kar","Telangana","MH","TN"],"City":["Beng","Hyd","Mum","Chennai"]}
print("State and City are:",dict)
print("States data",dict.get("States"))
print("City data",dict.get("City"))
print("again States data is:",dict["States"])

print(dict)

import pandas as pd
df=pd.DataFrame(dict)
print(df)
print("1"*50)
#for placeholder_variable in sequence:
    # code that does something
for char in 'Sequence Genarator':
    print(char)


for i in range(1,11):
    for j in range(1,11):
        print("i*j",i,j,i*j)

programming_languages = ["Python", "JavaScript", "Java", "C++"]

# iterate over each item in the list
for language in programming_languages:
  print(language)