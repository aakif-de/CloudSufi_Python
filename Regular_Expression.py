import re
text='Ema is very sweet good girl'
x=re.finditer(r'g',text)
for i in x:
    print(i)