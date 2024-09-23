list=[2,2,1,1,1,2,2,3,3,5,4,7,8,8,4,5,6,2]
count=dict()
for i in list:
    if i in count:
        count[i] += 1   
    else:
        count[i] = 1
print (max(count.values()))
