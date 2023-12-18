'''This file created to practice logical operator
Author - Sreeni added date:18/Dec/2023 '''

#and, or, not

#AND
#if both condition true --> True
#if one condition false then   --> False
# OR
#if one condition true --> True
#if both condition false then   --> false

a=10
b=20
c=30

if a<b and a<c:
    print(" a is the smallest number")

if a<b or a>c:
    print("a is less than b")
else:
    print("both conditions false")


a = 10
b = 20
print('#'*30)
if not(a>b):
    print("a is greater than b")
elif  a<b:
    print("a is less than b")



