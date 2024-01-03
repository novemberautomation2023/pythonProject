'''This file created to exceptions
Author - Sreeni added date:02/Jan/2024 '''

# 1. Syntax error
# 2. Runtime error

# print("This is print stmt")
#
# for i in range(1,10):
#     print(i)
#
# def test():
#     print("hello")

a = 10
b = 0
#print(a/b)
try:
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
except ZeroDivisionError as msg:
    #print(a/a)
    print("This is Zero division error while performing a/b", msg)
except TypeError as msg:
    #print(a/a)
    print("This is type error when performing a-b or a+b", msg)
except NameError as msg:
    #print(a/a)
    print("Name error exception", msg)
except:
    print(" May be one of the value is missing")
finally:
    print("This is finally block")

