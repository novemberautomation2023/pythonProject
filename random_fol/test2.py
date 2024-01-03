# a = int(input("enter a value:"))
#
# b = int(input("enter b value:"))

try:
    print(100/0)
except ZeroDivisionError as msg:
    print("Enter correct a and b value")
except TypeError:
    print("this is type error")
except:
    print("this is default except block")
finally:
    print("finally")



