#convert as a function
def func(ValidP):
    list=[]
    for i in validP:
        if i in '([{':
            list.append(i)
        elif not list:
            return False
        elif i==')':
            if list.pop() != '(':
                return False
        elif i=='}':
            if list.pop() != '{':
                return False
        elif i==']':
            if list.pop() != '[':
                return False
    if list:
        return False
    return True
validP="(){"
print(func(validP))