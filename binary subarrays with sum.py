class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixCounts = collections.defaultdict(int)
        prefixCounts[0] = 1
        prefix = 0 
        count = 0
        for num in nums:
            prefix+=num
            count += prefixCounts[prefix-goal]
            prefixCounts[prefix]+=1
        return count
