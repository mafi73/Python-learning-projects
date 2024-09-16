#leetcode
#https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6,]
n = 3
nums1=(nums1+nums2)
nums1.sort()
n=n+m
nums1=nums1[-n:]
print(nums1)        