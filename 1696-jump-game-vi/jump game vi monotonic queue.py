class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        maxQue = deque([[nums[-1],len(nums)-1]])
        
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)-2, -1, -1):
            if i == 0:
                while i+k<len(nums) and maxQue[0][1] > i+k:
                    maxQue.popleft()
                return maxQue[0][0] + nums[0]
            while i+k<len(nums) and maxQue[0][1] > i+k:
                maxQue.popleft()
            temp = maxQue[0][0]
            while maxQue and maxQue[-1][0] < maxQue[0][0] + nums[i]:
                maxQue.pop()
            maxQue.append([temp + nums[i], i])
        
