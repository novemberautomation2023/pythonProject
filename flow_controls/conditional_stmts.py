'''This file created to practice conditional statements
Author - Sreeni added date:19/Dec/2023 '''

#syntax for if conditinal statment
#if condition:code/statments

name = 'Sreeni'
if name == 'Sreeni':
    print("Hello sreeni, Good morning")
    print("Hello sreeni, How are you?")

#syntax for if and else conditinal statment
#if condition:
#  code/statments
#else:
#    code

name = input("Enter name of the Guest: ")
print("the type of name", type(name))
print("The value of name", name)
if name == 'Sreeni':
    print("Hello sreeni, Good morning")
    print("Hello sreeni, How are you?")
else:
    print("hello Guest, Good morning")

# if-elif-else
#syntax for if , elif and else conditinal statment
#if condition:
#  code/statments
#elif condition:
# code/Statement
#else:
#    code

name = input("Enter name of the Guest: ")
print("the type of name", type(name))
print("The value of name", name)
if name == 'Sreeni':
    print("Hello sreeni, Good morning")
elif name == 'Raghav':
    print("Hello Raghav, Good morning")
elif name == 'Balaji':
    print("Hello Balaji, Good morning")
else:
    print("hello Guest, Good morning")

# if-elif
#syntax for if and else conditinal statment
#if condition:
#  code/statments
#elif condition:
# code/Statement
name = input("Enter name of the Guest: ")
if name == 'Sreeni':
    print("Hello sreeni, Good morning")
elif name == 'Raghav':
    print("Hello Raghav, Good morning")
elif name == 'Balaji':
    print("Hello Balaji, Good morning")

# if
# if-else
# if-elif-else
# if-elif
# elif-else

# 1 --> one
# 2 --> two
# 3 --> Three
# 9 --> nine

number = int(input("enter number: "))

if number == 1:
    print("one")
elif number == 2:
    print("two")
elif number == 3:
    print("three")
elif number == 4:
    print("four")
elif number == 5:
    print("five")
elif number == 6:
    print("six")
elif number == 7:
    print("seven")
elif number == 8:
    print("eight")
elif number == 9:
    print("nine")
elif number == 0:
    print("zero")
else:
    print("Enter more than one digit number")

# Identify biggest number from these 3 numbers ( 10,20,30)
# Identify smallest number from these 3 numbers ( 10,20,30)


