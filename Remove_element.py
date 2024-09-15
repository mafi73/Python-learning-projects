#Remove Element
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

l=[1,2,2,3,6,3,4,5,8,5,4,5,6]
b=6
i=0
while i < len(l):
    if l[i]==b:
        l.remove(l[i])
    else:
        i+=1
print(l) 

#leetcode solve code:
#class Solution:
#    def removeElement(self, nums: List[int], val: int) -> int:
#        i=0
#        while i < len(nums):
#            if nums[i]==val:
#                nums.remove(nums[i])
#            else:
#                i+=1
#        return len(nums)
