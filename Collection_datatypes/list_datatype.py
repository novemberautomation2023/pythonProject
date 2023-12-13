'''This file created to practice list DT
Author - Sreeni added date:08/Dec/2023'''


ls = [1,2,3,'Sreeni','Balaji',10.5,1+2j, True]

print(ls)
print(type(ls))
print("ls[0]", ls[0])
print("ls[1]", ls[1])
print("ls[2]", ls[2])
print("ls[3]", ls[3])
print("ls[4]", ls[4])
print("ls[5]", ls[5])
print("ls[6]", ls[6])
print("ls[7]", ls[7])
print("ls[0:3]", ls[0:3])
print("ls[-1]", ls[-1])
print("ls[0:7:2]", ls[0:7:2])
print("type ls", type(ls))
print("type ls[0]",ls[0], type(ls[0]))
print("type ls[3]",ls[3], type(ls[3]))
print("type ls[5]",ls[5] ,type(ls[5]))
print("type ls[7]",ls[7], type(ls[7]))

ls2 = [1,2,3,1,3]
print(type(ls2))
print(ls2)

print(dir(ls))

ls = [1,2,3]
print("before append",ls)
ls.append(5)
print("after append",ls)
ls.append([4,5])
print("after adding 4,5", ls)
ls.extend([7,8,9])
ls.extend([10])
print("after extend 7,8,9", ls)

print("before pop", ls)
ls.pop(4)
print("after pop", ls)
ls.pop()
print("after pop()", ls)

ls[0]=25
print("after ls[0]=25", ls)

ls.insert(3,'sreeni')
ls.insert(100,'sreeni7')

print("after insert sreeni",ls)

ls= [1,5, 2,2,3,3,3,4,5,5,5,5,5,5]
print(ls.count(5))

ls.reverse()

print("after reverse", ls)


ls = [5,2,1,4,'sreeni',1,6,'sreeni']
print(ls)
#ls.sort()
print("after sort", ls)

ls.remove('sreeni')
print("after remove",ls)



