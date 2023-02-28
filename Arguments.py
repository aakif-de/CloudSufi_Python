#keyword variable length argument
def person(name,**data):
    print(name)
    print(data)
person('aakif',age=28,city='faridabad',phone_no=98118581)