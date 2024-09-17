#leetcode
#https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
#راه حل دوم بدون استفاده از متد سورت کردن
lass Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pn1=m-1
        pn2=n-1
        pw=m+n-1
        while pw >=0:
            if pn1<0:
                nums1[pw]=nums2[pn2]
                pw-=1
                pn2-=1
            elif pn2<0:
                nums1[pw]=nums1[pn1]
                pw-=1
                pn1-=1
            elif nums2[pn2]>nums1[pn1]:
                nums1[pw]=nums2[pn2]
                pn2-=1
                pw-=1
            else:
                nums1[pw]=nums1[pn1]
                pn1-=1
                pw-=1
