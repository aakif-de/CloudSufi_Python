abc=10
print(abc)
name='AAKIF'
print(name)
print()
a='youtube'
print(a[5])
print(a[-1])  #Reverse indexing
print(a[1:3])  #Here 1 is the start indexing and 3 is the indexing till we have to print
print(a[0:])  #Start from 0 and will print till last character of string
print("my" + a[3:])  #Will print mytube.
#Global Variable
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#Local Variable
x = "awesome"
def myfunc1():
  x = "fantastic"
  print("Python is " + x)
myfunc1()
print("Python is " + x)