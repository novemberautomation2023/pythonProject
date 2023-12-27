'''This file created to practice functions
Author - Sreeni added date:26/Dec/2023 '''

# def sum(a,b): #arguements
#     print("the value of a ",a)
#     print("the value of b ",b)
#     print(f"Sum of {a} and {b}", a+b)
#     return a+b
#
#
# sum(10,20) # POSITIONAL ARGUMENTS
# print("#"*30)
# sum(b=10,a=20) # keyword argument
# print("#"*30)
# sum(5,b=6)
# print("#"*30)
# sum(22,b=11)
# print("#"*30)
# print(sum(2,b=3))
#
# def welcome( marks, name,college='SV' ):
#     print("Welcome "+ name + " belongs to " + college + " Marks " + str(marks) )
#
#
# welcome(34,"Sreeni")
# welcome(34,"Sreeni", college="SVU")
# welcome(34, name ='Sreeni', college="SVU")
#
# def welcome2():
#     print("Welcome to SVCE" )
#
# welcome2()
#
# #pos, key, def--> function call

# def cal(a,b):
#     addition = a+b
#     sub = a-b
#     mul = a*b
#     print(f"Sum of {a} and {b} is {addition}")
#     print(f"sub of {a} and {b} is {sub}")
#     print(f"multiplication of {a} and {b} is {mul}")
#     return addition,sub, mul
# cal(10,20)
#
# def cal(a,b,c):
#     addition = a+b+c
#     sub = a-b-c
#     mul = a*b*c
#     print(f"Sum of {a} , {b}, {c} is {addition}")
#     print(f"sub of {a} , {b},{c} is {sub}")
#     print(f"multiplication of {a} , {b}, {c} is {mul}")
#     return addition,sub, mul
#
# cal(10,20,30)


def cal(s1,*n):
    #print(type(n))
    #print(n)
    sum = 0
    sub = n[0]
    mul = 1
    for i in n:
        sum = sum+i
        mul = mul * i
        sub = sub - i
    print(f"The sum of {n} values is", sum)
    print(f"The mul of {n} values is", mul)

cal(10,20.0)
cal(10,20)
cal(10,20,33)
cal(10,20,33,55,76,99)
cal(10,2)












def sub(a,b, c=30): #arguements
    print("the value of a ",a)
    print("the value of b ",b)
    print(f"sub of {a} and {b}", a-b)