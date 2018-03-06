
import copy
a=[1,2,4,["ab","cd"]]
b=a
c=a[:]
d=copy.copy(a)
e=copy.deepcopy(a)

print(c,id(c))

print(d,id(d))

print(e,id(e))

print(a,id(a))
print(b,id(b))

