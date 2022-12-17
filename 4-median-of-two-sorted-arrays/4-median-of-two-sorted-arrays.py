class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+len(nums2)
        half = total // 2
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        l = 0
        r = len(nums1)-1
        while True:
            i = (l+r) // 2
            j = half-i-2
            nums1l = nums1[i] if i>=0 else -float('inf')
            nums2l = nums2[j] if j>=0 else -float('inf')
            nums1r = nums1[i+1] if i+1<len(nums1) else float('inf')
            nums2r = nums2[j+1] if j+1<len(nums2) else float('inf')
            if nums1l<=nums2r and nums2l<=nums1r:
                if total%2 == 1:
                    return min(nums1r,nums2r)
                else:
                    return (min(nums2r,nums1r)+max(nums1l,nums2l))/2
            elif nums1l>nums2r:
                r = i-1
            elif nums2l>nums1r:
                l = i+1