class College:
    college_name='SVCE'
    """This is calculator function"""
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
        College.principle='DR. Ramachandra'

    def student_info(self):
        College.dept='XYZ'
        print(f"student id is {self.id}, name is {self.name},"
              f" marks are {self.marks}", {self.college_name},
              self.principle , self.dept)
    @classmethod
    def college_info(cls):
        print(f"college name is {cls.college_name}")




obj = College(1,'sreeni',75)

print(obj.student_info())




