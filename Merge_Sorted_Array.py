nums1 = [1,2,3,5,0,0,0,0]
m = 4
nums2 = [2,5,6,0,0]
n = 3
nums1=(nums1+nums2)
nums1.sort()
n=n+m
nums1=nums1[-n:]
print(nums1)        