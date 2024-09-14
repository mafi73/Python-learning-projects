array=[1,2,2,3,3,3,4,6,6,6,6]
i=0
c=0
while i<len(array):
    if array[i]==array[i+1]:
        array.pop(array[i])
        i+=1
        c+=1
    else:
        i+=1
print(array)
print(c)
