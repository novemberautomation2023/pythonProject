
class College:
    college_name = 'SVCE' # class variable
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
        College.principal = 'Dr. Arvind' # class variable
        print("class variable college name is printed in con method using self",self.college_name)
        print(" class variable college name is printed in con method using class name", College.college_name)

    def student(self):
        College.hod='Ramesh' # class variable
        print("class variable college name is printed in student method using self", self.college_name)
        print(" class variable college name is printed in student method using class name", College.college_name)

    @classmethod
    def college_info(cls):
        cls.branch = 'BSC'  # class variable
        College.branch2='CSE' # class variable
        print("class variable college name is printed in college info method using cls", cls.college_name)
        print(" class variable college name is printed in college info method using class name", College.college_name)

    @staticmethod
    def total_per():
        College.percentage =78 # class variable

obj = College('Sreeni',35)

print(obj.__dict__)
print(College.__dict__)
obj.student()
print(obj.__dict__)
print(College.__dict__)
obj.college_info()
print(obj.__dict__)
print(College.__dict__)

obj.total_per()
print(obj.__dict__)
print(College.__dict__)
#
# print(obj.college_name) # class variable access out of class using object referecene
#
# print(College.college_name) # class variable access out of class using class name