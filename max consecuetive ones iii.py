class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        zeros = []
        maxLen = 0
        while j<len(nums):
            if nums[j] == 0 and k>0:
                k-=1
                zeros.append(j)
            elif nums[j] == 0 and k == 0:
                if len(zeros)>0:
                    i = zeros.pop(0)+1
                    zeros.append(j)
                else:
                    i = j+1
            maxLen = max(maxLen,j-i+1)
            j+=1
        return maxLen
            
            
            
