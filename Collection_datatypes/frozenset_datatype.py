'''This file created to practice frozenset DT
Author - Sreeni added date:13/Dec/2023 '''

fs = frozenset({1,2,3})

print(type(fs))

print(dir(fs))

#Union method
fs1 = frozenset({1,2,3,4,7})
fs2 = frozenset({4,5,6,1})

print("fs1.union(fs2) union operation",fs1.union(fs2))
print("fs1.difference(fs2) difference operation",fs1.difference(fs2))
print("fs2.difference(fs1) difference operation",fs2.difference(fs1))

fs2.add(5)