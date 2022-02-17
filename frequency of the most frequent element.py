class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        i=1
        j=0
        freq = 1
        highestFreq = freq
        while i < len(nums):
            if k - (nums[i]-nums[i-1])*freq >= 0:
                k -= (nums[i] - nums[i-1])*freq 
                i+=1
                freq += 1
                if freq > highestFreq:
                    highestFreq = freq
            elif freq > 1:
                k += nums[i-1] -nums[j]
                freq -= 1
                j+=1
            else:
                j+=1
                i+=1
        return highestFreq
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
