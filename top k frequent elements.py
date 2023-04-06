class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = list(counts.keys())
        self.soln = []
        helper(arr,self,k,counts)
        return self.soln
        
def helper(arr,obj,k,freq):
    mid = len(arr)//2
    currNum = arr[mid]
    left = []
    right  = []
    for num in arr:
        if freq[num] <= freq[currNum] and num!=currNum:
            left.append(num)
        elif freq[num] > freq[currNum]:
            right.append(num)
    if len(right)>k:
        helper(right,obj,k,freq)
    elif len(right) == k:
        obj.soln.extend(right)
    else:
        obj.soln.extend(right)
        obj.soln.append(currNum)
        if len(right)+1 < k:
            helper(left,obj,k-len(right)-1,freq)
            

    




# class Solution(object):
#     def topKFrequent(self, nums, k):
#         nums.sort()
#         freq = 0
#         frequencies = []
#         temp = nums[0]
#         values = [temp]
#         freqValues = []
#         answer = []
#         for i in range(len(nums)):
#             if nums[i] == temp:
#                 freq += 1
#             if nums[i] != temp or i == len(nums) - 1:
#                 temp = nums[i]
#                 values.append(temp)
#                 frequencies.append(freq)
#                 freq = 1
#         frequencies.append(freq)
#         for i in range(len(values)):
#             freqValues.append([frequencies[i], values[i]])
#         i = 1
#         freqValues.sort()
#         while i <= k:
#             answer.append(freqValues[-i][1])
#             i += 1

#         return answer
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
        
