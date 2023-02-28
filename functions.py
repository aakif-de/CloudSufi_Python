#functions
def greet():  #Syntax: def keyword followed by function name then () followed by :
    print('Aakif')

greet()  #calling our greet() function
greet()  #we can call our function multiple times.and need not to-write code again

def add(a,b):
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    c=a+b
    print(c)
add('a','b')
#Return type function
#Return single value
def mul(a,b):
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a*b
    return c
result=mul('a','b')
print(result)
#return two/multiple values
def sub_div(x,y):
    x=int(input("enter first number"))
    y =int(input("enter second number"))
    z=x-y
    k=x//y
    return z,k
result1,result2=sub_div('x','y')
print(result1,result2)