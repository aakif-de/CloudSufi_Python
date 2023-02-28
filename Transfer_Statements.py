#Transfering Statements
#break
available=5
x=int(input("Enter the no of candies you want"))
i=1
while i<=x:
    if i>available:
        print("not have enough candies")
        break
    print("candy")
    i+=1
#Continue
#Continue
#To print values from 1-100 and skip those who are divisible by 3
for i in range(1,101):
    if i % 3==0:
        continue
    print(i)
#pass
a = 10
b = 20
if(a>b):
    pass
else:
    print("b is greater")
