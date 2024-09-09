#convert as a function
s=input('please give a string? ')
list=[]
for i in s:
    if i in '([{':
        list.append(i)
    elif not list:
        print ('False')
    elif i==')':
        if list.pop() != '(':
            print ('False')
    elif i=='}':
        if list.pop() != '{':
            print ('False')
    elif i==']':
        if list.pop() != '[':
            print ('False')
if list:
    print ('False')
print (True)