class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        nums.append(0)
        left = -1
        maxAvg = float('-inf')
        summ = 0
        for right in range(len(nums)-1):
            summ+=nums[right]
            if right >= k-1:
                summ-=nums[left]
                maxAvg = max(maxAvg,summ/k)
                left+=1
        return maxAvg
