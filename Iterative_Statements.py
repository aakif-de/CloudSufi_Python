#While loop
i=0   #Initialisation
while i<5:  #Condition
    print("Aakif",end=" ")
    i+=1  #Increment
#NESTED While
i=0
while i<5:
    print('Aakif',end=" ")
    j=0
    while j<5:
        print("khan",end=" ")
        j+=1
    i+=1
    print()
#For Loop
x=range(1,10)
for i in x:
    print(i)
#2 If number is divisible by 5 don't print
for i in range(1,21,1):
    if i % 5!=0:
        print(i)
