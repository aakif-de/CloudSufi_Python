#Swapping
a=5
b=6
c=b
b=a
a=c
print(a,b)
#2 Way
a=5
b=6
a=a^b
b=a^b
a=a^b
print(a,b)
#3 Way
a=5
b=6
a,b = b,a
print(a,b)