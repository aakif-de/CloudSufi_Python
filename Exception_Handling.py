a=5
b=2
try:
    print('resoruce_open')
    print(a/b)
    k=int(input("enter the value "))
except ZeroDivisionError as e:
    print('Cant divide by 0',e)
except ValueError as e:
    print('Invalid Input',e)
except Exception as e:
    print('something went wrong',e)
finally:
    print('resource close')
