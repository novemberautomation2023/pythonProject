'''This file created to practice String functions
Author - Sreeni added date:06/Dec/2023'''

str = 'Sreeni'

str2 = 'Balaji'

print(dir(str))

print(dir(str2))

a = 10

print(dir(a))


str = 'sreEnivas KattuBadi '

print("str.capitalize()", str.capitalize())
print("str.center", str.center(50))

print("This is comment".center(40))

print("str.casefold()", str.casefold())
print("str.lower()", str.lower() )

str= 'Sreenivas kattubadi'

print("str.upper()" , str.upper())


str = ' Sreeni  ka   '
print("str.lstrip()" , str.lstrip()) #ltrim # default - space
print("str.rstrip()" , str.rstrip()) #rtrim
print("str.strip()" , str.strip()) #trim

str = '123Sreeni  ka123'
print("str.lstrip('123')" , str.lstrip('12')) #ltrim # default - space
print("str.rstrip('123')" , str.rstrip('a123')) #rtrim
print("str.strip('123')" , str.strip('123')) #trim

str = 'ababcdefghabfg'
print("str.strip('ab')" , str.strip('ab'))

str = '156seenu'
print("str.strip('[0-9]')" , str.strip('0123456789')) #ltrim # default - space # I will check

print("str.replace('156','S')",str.replace('156','S'))


# s="Hello347 Python3$"
# import re
# s1=re.sub("[0-9]","",s)
# print("s1", s1)

str = 'Balaji venkateshanj'

print("str.endswith()", str.endswith('shan'))
print("str.endswith()", str.endswith('i'))
print("str.startswith()", str.startswith('Bal'))
print("str.startswith()", str.startswith('b'))
print("str.find('j')", str.find('j',6, 10))


txt = "Hello Sreeni!"
print(txt.translate(str.maketrans("Ser","POi")))

str = 'Hello world 1234' # Alphabets and numeric[ a-z , A-Z , 0-9]

print("str.isalnum()", str.isalnum())

str2 = 'Helloworld1234' # Alphabets and numeric[ a-z , A-Z , 0-9]

print("str2.isalnum()", str2.isalnum())

#Name - fn, ln, full, suffix, prefix
#Phone - Numbers
str3 = "Sreeni"
print("str3.isalnum()", str3.isalpha())
str4 = "Sreeni123@"
print("str4.isalnum()", str4.isalpha())
phone = '9763536441'
print("phone.isalnum()", phone.isdigit())
phone2 = '976353644!'
print("phone2.isalnum()", phone2.isdigit())

str = 'test123'
print("str.isidentifier()", str.isidentifier())

str = 'Hello world, Welcome to python class,I have Intermediate level of knowledge in python'
print("Split function", str.split('o'))

str2 = 'This is sreeni#I have 9 year exp # I have exp in etl testing # I have also automation exp'
print("Split function", str2.split('#',2))

dtypes1 = ["column1", "column2", "column3"]
print(type(dtypes1))
x = ",".join(dtypes1)
print(x)
print(type(x))

dtypes1 = ["column1", "column2", "column3"]
print(type(dtypes1))
columns = ",".join(dtypes1)

query = "select " + columns + " from table"
print(query)
print(type(query))

s = 'foo'
t = 'bar'
print(2 * (s + t))
print('iarf' in 2 * (s + t))

#print(ord('foo'))


str = 'Sreenivas'

print(str[::-1])

print(str[::-2])

s = 'foobar'
print(s[::-1][-1] + s[len(s)-1])

print(
    '$100 $200 $300'.count('$'),
    '$100 $200 $300'.count('$', 5, 10),
    '$100 $200 $300'.count('$', 5)

)










