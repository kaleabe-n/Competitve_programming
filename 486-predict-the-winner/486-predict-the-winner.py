class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        return helper(0,len(nums)-1,nums,dp)>=0
        
def helper(l,r,nums,dp):
    if r == l:
        return nums[l]
    if (l,r) in dp:
        return dp[(l,r)]
    left = nums[l] - helper(l+1,r,nums,dp)
    right = nums[r] - helper(l,r-1,nums,dp)
    dp[(l,r)] = max(left,right)
    return max(left,right)


# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         dp = {}
#         def chooseBest(left,right,dp):
#             if left == right:
#                 return nums[left]
#             if (left,right) in dp:
#                 return dp[(left,right)]
#             bestLeft = nums[left] - chooseBest(left+1,right,dp)
#             bestRight = nums[right] - chooseBest(left,right-1,dp)
#             dp[(left,right)] = max(bestLeft,bestRight)
#             return max(bestLeft,bestRight)
#         return chooseBest(0,len(nums)-1,dp)>=0
        
