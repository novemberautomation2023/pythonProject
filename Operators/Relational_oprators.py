'''This file created to practice range DT
Author - Sreeni added date:14/Dec/2023 '''

a = 10
b = 10
print("the value of a ", a)
print("the value of b ", b)

print("a>b ", a>b)
print("a>=b ", a>=b)
print("a<b ", a<b)
print("a<=b ", a<=b)
print("a==b ", a==b)
print("a!=b ", a!=b)

name = "Raghav"
# = is assignment opearator
#  == is compare opearator

if name == 'sreeni':
    print("Hello Sreeni, Good morning!")
elif name != 'sreeni':
    print("hello Guest, Good morning")

age=18

if age>=18:
    print("Eligible for vote")
elif age<18:
    print("Not eligible")

source_cnt = 20
target_cnt = 21
if source_cnt == target_cnt:
    print("count ts is passed")
else:
    print("count ts is failed")

def dodo(b):
    b= b+'2'
    b=b*2
    print(b)

dodo("Whale")

print

print(id(dodo))
