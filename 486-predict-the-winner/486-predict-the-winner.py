class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def chooseBest(left,right,dp):
            if left == right:
                return nums[left]
            if (left,right) in dp:
                return dp[(left,right)]
            bestLeft = nums[left] - chooseBest(left+1,right,dp)
            bestRight = nums[right] - chooseBest(left,right-1,dp)
            dp[(left,right)] = max(bestLeft,bestRight)
            return max(bestLeft,bestRight)
        return chooseBest(0,len(nums)-1,dp)>=0
        