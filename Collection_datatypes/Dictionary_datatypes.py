'''This file created to practice Dictionary DT
Author - Sreeni added date:14/Dec/2023 '''

d = {}

print("type(d)",type(d))

d2 = {1:"Sreeni",2:"Ramesh", 3:"Rahul"}
print("type(d2)",type(d2))

print("Data inside d dict",d)
print("Data inside d2 dict",d2)

print(dir(d2))

# Keys and values
print("Key available in d2 ", d2.keys())
print("values available in d2 ", d2.values())
print("Keys and values available in d2 ", d2.items())

d2 = {1:"sreeni", 2:"ramesh", 1:"Ram", 3:"ramesh"}
print(" Dictionary d2 values", d2)

# Adding new values and update existing values
d3 = { 1:"ramesh", 2:"Ram", 3:"ramesh"}
print("Before adding key 4 to d3", d3)
d3[4] = 'Ind'
d3[2] = 'Ramnath'
print("After adding key 4 to d3", d3)

# Adding new values and update existing values using update

print("Before adding key 5 to d3", d3)
d3.update({5:"Somesh"})
d3.update({3:"Upendra"})
print("After adding key 5 to d3", d3)

# Accessing the values from the dictionary
print("dictionary d3", d3)
print("d3.get(5)", d3.get(5))
print("d3.get(4)", d3.get(4))

print("d3[2]", d3[2])
#print("d3[10]", d3[10])

#remove the elements from dictionary
print("before pop dictionary d3", d3)
print("d3.pop(1)", d3.pop(1))
print(" after pop dictionary d3", d3)


#remove the elements from dictionary
print("before popitem dictionary d3", d3)
print("d3.popitem", d3.popitem())
print(" after popitem dictionary d3", d3)

d4 = {"fruits":["Mango","apple","guava"], "vegetables":["Tomoto", "onion","brinjal"]}

print("fruits data",d4.get(1))
#print("fruits data",d4[1])
print("Type of fruits data",type(d4.get("fruits")))
# print("before pop d4", d4)
# d4.pop("fruits")
# print(" after pop d4",d4)

import pandas as pd
df = pd.DataFrame(d4)
print(df)



#





# Adding new values and update existing values
d3 = { 1:"ramesh", 2:"Ram", 3:"ramesh"}
print("Before adding key 4 to d3", d3)
d3[4] = 'Ind'
d3[2] = 'Ramnath'
print("After adding key 4 to d3", d3)

# Adding new values and update existing values using update

print("Before adding key 5 to d3", d3)
d3.update({5:"Somesh"})
d3.update({3:"Upendra"})
print("After adding key 5 to d3", d3)

# Accessing the values from the dictionary
print("dictionary d3", d3)
print("d3.get(5)", d3.get(5))
print("d3.get(4)", d3.get(4))

print("d3[2]", d3[2])
#print("d3[10]", d3[10])

#remove the elements from dictionary
print("before pop dictionary d3", d3)
print("d3.pop(1)", d3.pop(1))
print(" after pop dictionary d3", d3)


#remove the elements from dictionary
print("before popitem dictionary d3", d3)
print("d3.popitem", d3.popitem())
print(" after popitem dictionary d3", d3)

d4 = {"fruits":["Mango","apple","guava"], "vegetables":["Tomoto", "onion","brinjal"]}

print("fruits data",d4.get(1))
#print("fruits data",d4[1])
print("Type of fruits data",type(d4.get("fruits")))
# print("before pop d4", d4)
# d4.pop("fruits")
# print(" after pop d4",d4)

import pandas as pd
df = pd.DataFrame(d4)
print(df)



