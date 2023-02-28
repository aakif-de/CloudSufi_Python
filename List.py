list_A=[1,2,'Aakif',10,5,'khan',-2]
print(list_A)
list_A.append(20)  #Adding Value at the end
print(list_A)
list_A.reverse()  #Reverse the list
print(list_A)
list_A.pop(0)
print(list_A)  #Remove the element from a particular indexing
list_A.insert(0,77)  #Insert at particular indexing
print(list_A)
list_A.remove(77)  #Remove that particular value
print(list_A)
list_A.extend([5,10,15,20])  #To add multiple values
print(list_A)

list_B=[1]
list_B.extend([2,3,4,5,6,7])
print(list_B)
print(max(list_B))
print(min(list_B))
print(sum(list_B))
list_B[0]=10  #We can change values
print(list_B)