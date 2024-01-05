

class college:
    def __init__(self,name,marks):
        self.name=name # instance vaiable
        self.marks=marks # instance variable
        print("This marks coming from const",self.marks)
    def student(self): # instance method
        self.department='ECE'  # instance variable
        self.dept2='CSE'
        print("This name coming from student method",self.name)
        print("This marks coming from method",self.marks)
    def lecturer(self): # instance method
        self.lecturer_name='Janav'  # instance variable
        del  self.name

    @classmethod
    def college_info(cls,marks): # class method
        #pass
        print("This marks coming from college info method",marks)
    @staticmethod
    def total_per(): # static method
        no_of_student = 10 # local variables
        percent = 78 # local variable
        #print(self.name)


obj = college('sreeni', 90)
print(obj.__dict__)

# del obj.marks
#
# print(obj.__dict__)
#
# del obj.name
# print(obj.__dict__)

obj.student()
print(obj.__dict__)

obj.lecturer()
print(obj.__dict__)

obj.college_info(70)




# obj = college('Sreeni',76)
# obj.student()
# obj.college_info()
# obj.total_per()
#
# print("This name coming from outside class using obj reference", obj.name)
# print("This marks coming outside class using obj reference", obj.marks)
#




# print(obj.__dict__)
# obj.student()
# print(obj.__dict__)
# obj.lecturer()
# print(obj.__dict__)
# obj.lecturer2 = 'Ramesh'
# print(obj.__dict__)
# obj2 = college('rahul',90)
# print(obj2.__dict__)
# obj2.student()
# print(obj2.__dict__)
# obj2.lecturer()
# print(obj2.__dict__)
#
# obj2 = college('Sreeni',76)