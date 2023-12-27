'''This file created to lambda functions
Author - Sreeni added date:27/Dec/2023 '''

#lamda lis_of_arguments : expression

cal = lambda a,b: a+b

print(cal(10,20))
print(cal(100,200))
s= lambda a,b: a if a>b else b
print(s(10,12))
l2 = lambda col: col.strip().upper()
print(l2(' name '))




