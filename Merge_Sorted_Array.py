nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1=nums1+nums2
for i in nums1:
    if i==0:
        nums1.remove(i)
print(nums1)        