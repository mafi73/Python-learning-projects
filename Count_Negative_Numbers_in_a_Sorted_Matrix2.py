#Leetcode 

#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
#Count Negative Numbers in a Sorted Matrix
matrix = [[4, 3, 2, -1],[3, 2, 1, -1],[1, 1, -1, -2],[-1, -1, -2, -3]]
row = len(matrix) #tedade satrha
column = len(matrix[0]) #tedade sotoonha
c = 0
prow = 0 # shroro az satr 0(avval) sotone akhar (bala samt rast)
pcolumn = column - 1 #satr avval sotone akhar
while (prow < row) and (pcolumn >= 0):
    if matrix[prow][pcolumn] < 0: #satrha ta paiin manfi an
        c += (row - prow) #az oun satr be paiin hamash manfi ast
        pcolumn -= 1  # harekat be sotone ghabl
    else:
        prow += 1  # satre paiin check mishet 
print(c)


