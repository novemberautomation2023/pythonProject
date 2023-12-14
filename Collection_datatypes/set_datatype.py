'''This file created to practice set DT
Author - Sreeni added date:13/Dec/2023 '''

s = {1,3,2,'string', 10.5, 1+2j, True,2,3}

print(type(s))
print(s)
s1 = set()
s2 = {}
print("type(s1)", type(s1))
print("type(s2)",type(s2))
print(dir(s1))

#Add Methods
print("before adding",s)
s.add(6)
print("after adding" ,s)





#Pop Methods
print("before pop",s)
s.pop()
print("after pop" ,s)
s.pop()
print("after second pop" ,s)


#remove Method
print("before remove",s)
s.remove(10.5)
print("after remove" ,s)

#update Method
print("before update",s)
s.update([1,2,55])
print("after update" ,s)

#clear Methods
print("before clear",s)
s.clear()
print("after clear" ,s)

#Union method
s1 = {1,2,3,4,7}
s2 = {4,5,6,1}

print("s1.union(s2) union operation",s1.union(s2))
print("s1.difference(s2) difference operation",s1.difference(s2))
print("s2.difference(s1) difference operation",s2.difference(s1))



















