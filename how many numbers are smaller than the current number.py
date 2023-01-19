# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         max=0
#         for i in nums:
#             if i>max:
#                 max=i
#         freq=[0]*(max+1)
#         cumulativeFreq=[0]*(max+1)
#         for i in nums:
#             freq[i]=freq[i]+1
#         sum=0
#         for i in range(len(freq)):
#             sum+=freq[i]
#             cumulativeFreq[i]=sum
#         freq=[0]*len(nums)
#         for i in range(len(nums)):
#             if nums[i]==0:
#                 freq[i]=0
#             else:
#                 freq[i] = cumulativeFreq[nums[i]-1]
#         return freq


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        counts = collections.Counter(nums)
        keys = sorted(counts.keys())
        cumulativeFreqs = {}
        freq = 0
        smallerArr = []

        for key in keys:
            cumulativeFreqs[key] = freq
            freq += counts[key]

        for num in nums:
            smallerArr.append(cumulativeFreqs[num])
        
        return smallerArr

        
