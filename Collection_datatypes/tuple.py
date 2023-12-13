'''This file created to practice tuple DT
Author - Sreeni added date:12/Dec/2023'''

t = (1,2,3,'Sreeni',10.8,1+2j, True)
print(" first t",id(t))

t = ('a', 'b','c')
print("second t after overwrite",id(t))



print(type(t))
print("methods available in tuple",dir(t))
ls = [1,2,3,'Sreeni',10.8,1+2j, True]
print(type(ls))
print("methods available in list",dir(ls))

ls[0] = 500

print("updated list ", ls)

#t[0] = 500

#print("updated tuple ", t)

#t.pop()

ls = [1,2,3]

print("before update",id(ls),ls)


ls[2]=400
ls.append([5])
print("after update",id(ls),ls)





