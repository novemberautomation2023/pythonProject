class calculator:
    """This is calculator function"""
    def __init__(self):
        self.a = 100
        self.b = 200
        print(id(self))
        print("This is constructor")
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return  self.a/self.b

obj = calculator()
print(id(obj))

print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())

str ='Sreeni'
obj.c=100
calculator.d=1000

print(calculator.__dict__)

help(calculator)

