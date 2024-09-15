#Remove Duplicates from Sorted Array
array=[1,1,2,2,3,3,3,4,6]
i=0
c=0
while (i+1)<len(array):
    if array[i]==array[i+1]:
        array.remove(array[i])
        #OR--> array.pop(i)  # Remove the element at index i

        c+=1
    else:
        i+=1
print(array) #print array without duplicate
print(c) #number of duplicated numbers
