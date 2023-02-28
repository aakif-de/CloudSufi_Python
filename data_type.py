#Type function is used to check the data type
#NONE
print(None)
#NUMERIC
num=5
print(type(num))  #int
num=2.5
print(type(num))  #float
num=2+2j
print(type(num))  #Complex[ Real + Imaginary ]
a=10
b=5
print(a<b)  #Boolean[Ture / False ]
#Changing The data types
e=complex(a)
print(e)
z=float(a)
print(z)
#SEQUENCE
A=[1,2,'aakif',2.8,-5]  #List
print(type(A))
B=(1,2,3,"Aakif",2.7,20)  #Tuple
print(type(B))
C={1,2,4,5,7,6,'Aakif',29,-30,2,2,2}  #Set
print(type(C))
D="Aakif"
print(type(D))   #String
print(list(range(0,10,2)))  #Range can take up-to 3 parameters
#Dictionary
student={1:'Aakif',2:'Amreen',3:'Nadil',4:'Aditya'}
print(type(student))
print(student.keys())  #Printring all set of keys
print(student.values())  #Priting all values
print(student[1])  #Fetching value with help of key