class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        arrScore = nums[0]
        for num in nums:
            arrScore = arrScore & num
        if arrScore!=0:
            return 1
        currScore = None
        count = 0
        for num in nums:
            if currScore == None:
                currScore = num
            else:
                currScore = currScore & num
            if currScore == 0:
                count += 1
                currScore = None
        return count
