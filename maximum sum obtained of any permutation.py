class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        for start,end in requests:
            prefix[start]+=1
            prefix[end+1]-=1
        prefix.pop()
        for i in range(1,len(nums)):
            prefix[i]+=prefix[i-1]
        prefix.sort()
        nums.sort()
        totalSum=0
        m=10**9+7
        for i in range(len(nums)):
            totalSum+=nums[i]*prefix[i]
            totalSum%=m
        return totalSum
