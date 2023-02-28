#Arithematic_Operations

print(2 + 3)  #Addition
print(2 - 3)  #Subtraction
print(2 * 3)  #Multiplication
print(5 / 2)  #Output in float value
print(5 // 2)  #Floor division integer output
print(2 ** 3)  #Power Off/Exponent 2x2x2
print(10 % 3)  #Modulus -Gives Remainder
print()
#ASSIGNMENT OPERATORS
x=2
print(x)
x+=2   #Similarly -=,*=,/=  operators can be performed
print(x)
x,y=3,4  #Single Line Assignment
print(x,y)
print()
#UNARY OPERATORS : Which Works on single operand
a=10
print(a)
print(-a)
a=-a
print(a)

#RELATIONAL OPERATORS
a=10
b=20
print(a>b)  #Grater than
print(a<b)  #Lesser than
print(a==b)  #Compare
c,d=5,5
print(c<=d)  #Lesser than Equals too
print(c>=d)  #Grater than Equals Too
print(c!=d)  #Not Equals Too
print()
#LOGICAL OPERATORS
a,b=5,10
c = a<6 and b<12
print(c)
d = a>10 or b==10
print(d)
print(not(d))