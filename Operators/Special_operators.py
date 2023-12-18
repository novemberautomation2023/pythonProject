'''This file created to practice special operator
Author - Sreeni added date:18/Dec/2023 '''

#1. Identity operator(Memory id comparison) is, is not
#2. Membership operator ( Membership of any value) in , not in

a = 10
b = 10
c = 10
d = 20
print("id of a ", id(a))
print("id of b ", id(b))
print("id of c ", id(c))
print("id of d ", id(d))
print("identity of a,b is", a is b)
print("identity of a,d is", a is d)
print("identity of a,b is not", a is not b)
print("identity of a,d is not ", a is not d)

ls = [1,2,3,4]
t = (1,2,3,5)

print("1 in ls", 1 in ls)
print("5 in ls", 5 in ls)
print("5 in t", 5 in t)
print("5 not in t", 5 not in t)



