class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = tuple(nums1)
        nums2 = tuple(nums2)
        dp = [[None,None] for _ in range(len(nums1))]
        return min(helper(0,0,nums1,nums2,dp),helper(0,1,nums1,nums2,dp))

    
def helper(i,rev,nums1,nums2,dp):
    if dp[i][rev]:
        return dp[i][rev]
    if i == len(nums1)-1 and rev:
        return 1
    if i == len(nums1)-1:
        return 0
    curr = float('inf')
    if not rev:
        if nums1[i]<nums1[i+1] and nums2[i]<nums2[i+1]:
            curr = min(curr,helper(i+1,0,nums1,nums2,dp))
        if nums1[i]<nums2[i+1] and nums2[i]<nums1[i+1]:
            curr = min(curr,helper(i+1,1,nums1,nums2,dp))
    else:
        if nums2[i]<nums1[i+1] and nums1[i]<nums2[i+1]:
            curr = min(curr,helper(i+1,0,nums1,nums2,dp))
        if nums2[i]<nums2[i+1] and nums1[i]<nums1[i+1]:
            curr = min(curr,helper(i+1,1,nums1,nums2,dp))
        curr += 1
    dp[i][rev] = curr
    return curr
