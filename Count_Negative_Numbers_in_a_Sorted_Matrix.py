matrix=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
c=0
for i in matrix:
    for j in i:
        if j < 0:
            c+=1
print (c)