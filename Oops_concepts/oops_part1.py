'''This file created to practice oops
Author - Sreeni added date:03/Jan/2024 '''
#syntax
# class classname:
#     def __init__(self): # constructor method optional
#         stmt1
#         stmt2
#     def method1(self): # instance method (Optional)
#         stmt3
#         stmt4
#     @classmethod # classmethod(optional)
#     def method(self):
#         stmt5
#         stmt6
#     @staticmethod    # static method(Optional)
#     def method3():
#         stmt7

class Calculator:
    """this class is created to do some arithmetic calculations"""
    def __init__(self):
        print("Inside constructor")
        print("Id of self is ", id(self))
    def add(self,a,b): # instance method
        return a+b
    def sub(self,a,b): # instance method
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

#syntax to create object
#object_name/referecen_variable = classname()
obj = Calculator() # Mthod1
print(obj.add(4,5))
print(obj.sub(4,5))
print(Calculator().add(4,10)) # Method2

obj2 = Calculator()

print(Calculator.__dict__)

#obj.add()

# = calculator()

#print(obj)

class Calculator2:
    """this class is created to do some arithmetic calculations"""
    def __init__(self,a,b):
        print("Inside constructor self id is ",id(self))
        self.a = a
        self.b = b
        self.c = 10
    def add(self): # instance method
        print("the memory of self in add", id(self))
        return self.a+self.b
    def sub(self): # instance method
        print("the memory of self in sub", id(self))
        return self.a-self.b
    def mul(self):
        #print("the memory of self in mul", id(self))
        return self.a*self.b
    def div(self):
        print("the memory of self in div", id(self))
        return self.a/self.b

    def power(self):
        return self.a**self.b

obj3 = Calculator2(4,5)
print("Obj3 id is", id(obj3))

print("The values available in obj3", obj3.__dict__)

obj5 = Calculator2(10,20)
print("Obj5 id is", id(obj5))

print(obj3.add())
print(obj3.sub())
print(obj3.mul())
print(obj3.div())
print(obj3.power())

# obj4 = Calculator2(5,15)
#
# print(obj4.add())
# print(obj4.sub())
# print(obj4.mul())
# print(obj4.div())
# print(obj4.power())

class count_val:
    def __init__(self,sourcedf, targetdf):
        self.sourcedf= sourcedf
        self.targetdf= targetdf

    def count_validation(self):
        src_cnt= self.sourcedf
        tgt_cnt = self.targetdf
        if src_cnt == tgt_cnt:
            print("Count is matching")
        else:
            print("count is not matching")













