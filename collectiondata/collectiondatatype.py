'''this file is to create for dire data type'''
d={}
print(type(d))
d1={1:'manju',2:'ram',3:'manu',5:'raj',6:'karthi'}
print("type(d1)",type(d1))
print("data inside d1 dict",d1)
d2={1,'manju',2,'ram',3,'manu',5,'raj',6,'karthi'}
print("data inside d2 dict",d2)
print(dir(d2))
print(dir(d1))
print("keys available in d1",d1.keys())
print("values available in d1",d1.values())
print("keys  and values available in d1",d1.items())
#adding new values
d1={1:'manju',2:'ram',3:'manu',5:'raj',6:'karthi'}
print("before adding key5",d1)
d1[5]='ant'
print("after adding key5",d1)
print("values available in d1",d1.values())
print("before adding value ram",d1)
d1["ram"]=2
print("after adding value ram",d1)
# adding new values using update
print("before adding key 6 to d1",d1)
d1.update({6:"manju"})
print("after adding key 6 to d1",d1)
print("before adding key 2 to d1",d1)
d1.update({7:"india"})
print("after adding key 7 to d1",d1)

#accessing the values from the dictionary
print("d1.get(6)",d1.get(6))
print("d1['ram']",d1['ram'])
print("d1.pop(1)",d1.pop(1))
print("after pop dictionary d1",d1)
print("d1.popitem",d1.popitem)
print("after popitem dictionary d1",d1)
d5={'fruits':['mango','banana','orange','guava'],'int'[1,2,7,8,9],'vegetables'['potato','beans'],'name'['ram','shyam','malli']}
print('type of fruits data',type(d5.get('fruits')))


