data={1:'Aakif',2:'Nadil',3:'Ahmed'}
print(data)
print(data[1])  #Priting the values by accessing the key
print(data.get(2,'Not found'))  #Will print not found if key doesn't exist
print(data.get(4,'Not found'))





keys=['Aakif','Sajad','Amreen','Nadil']
values=['Python','R','JS','Blockchain']
dictionary=dict(zip(keys,values))
print(dictionary)
dictionary['Asjad']='Devops'  #Adding Value
print(dictionary)
del dictionary['Asjad']  #Deleting Value
print(dictionary)