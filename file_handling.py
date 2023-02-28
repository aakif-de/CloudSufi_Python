#Reading a file
f=open('Mydata','r')
print(f.read())  #used to read all the lines in the file
print(f.readline())  #used to read a single line starting from first

z=open('abc','w')
#the open keyword will first check for the file with name abc
#if it is not present it will create one
z.write('Aakif')