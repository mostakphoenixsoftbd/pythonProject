# Tuple manipulation

name = (1,2,3,4,5)
# name[2]=7
print(name)

x = list(name)
x[2] = 90
name = tuple(x)
print(name)

