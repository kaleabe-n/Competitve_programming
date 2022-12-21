class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = sum(nums)
        expSum = 0
        i = 0
        while i<=len(nums):
            expSum+=i
            i+=1
        i = 0
        while i<=len(nums):
            if summ+i == expSum:
                return i
            i+=1
            
        