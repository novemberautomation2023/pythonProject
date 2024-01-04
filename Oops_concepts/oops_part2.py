'''This file created to practice oops
Author - Sreeni added date:04/Jan/2024 '''

class Cal:
    def __init__(self):
        print("no arg init")
    def __init__(self,a,b):
        print("two arg init")
    def __init__(self,a):
        print("one arg init")
    def add(self,**kwargs):
        sum=0
        for values in kwargs.values():
            sum=sum+values
        print(sum)
# obj = cal(10)
# obj.__init__(1)
# obj.__init__(2)
# print(obj.add(a=4,b=5,c=6,d=7))

class Test:
    def add(self):
        print("this is add method")
    def sub(self):
        print("this is sub method")

# obj = Test()
# obj.__init__()
# print(Test.__dict__)
# obj.add()
# obj.sub()

class College:
    college_name='SVCE' # class variable because it is created outside all methods
    principle = 'DR. Ramachandra'
    def __init__(self,id,name,marks):
        self.id=id # instance variable
        self.name=name # instance variable
        self.marks=marks # instance variable
        College.branch='BSC'

    def student_info(self): # this is instance method because we are using self
        College.hod='XYZ'
        self.gender='male'
        print(f"student id is {self.id}, name is {self.name},"
              f" marks are {self.marks}", {self.college_name},
              self.principle , self.dept)
    def student_talk(self):
        print("gender is", self.gender)
    @classmethod
    def college_info(cls):
        print(f"college name is {cls.college_name}, {cls.hod}")
    @staticmethod
    def add():
        a=10 # local variable
        b=20 # local variable




obj = College(1,'sreeni',75)
obj2 = College(2,'Rghav',90)

print(obj.student_info())




