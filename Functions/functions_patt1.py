# # '''This file created to practice functions
# # Author - Sreeni added date:25/Dec/2023 '''
# #
# # # Syntax
# #
# # # def function_name(): # def, fn() mandatory
# # #     stmt1
# # #     stmt2
# # #     stmt3
# # #     return(Optional)
# #
# # def sum_1():
# #     a = 10
# #     b = 20
# #     sum = a + b
# #     print("The Sum value from sum_1 function", sum)
# #
# # def sum_2(a,b):
# #     sum2 = a+b
# #     print("Sum value  from sum_2 function ", sum2)
# #
# # #sum_1()
# #
# # sum_2(50,20) ctrl + /
# # sum_2(70,40)
# # sum_2(22,33)
# # sum_2(44,10)
# #
# def cal(a,b):
#     addition = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     print(f"Sum of {a} and {b} is {addition}")
#     print(f"sub of {a} and {b} is {sub}")
#     print(f"multiplication of {a} and {b} is {mul}")
#     print(f"division of {a} and {b} is {div}")
#     return addition,sub, mul, div
#
# add, sub2, mul, div = cal(10,25)
# print(add)
# print(sub2)
# print(mul)
# print(div)
# #
# #
# #
# # #3! -- 1*2*3
result2=10
from math import factorial,sqrt


def factorial2(num):
    result=1
    for i in range(1,num+1):
        result=result*i
    #print(f"The factorial of {num} is {result} ")
    return result

factorial2(5)
factorial(4)

print(sqrt(4))
