class Solution(object):
    def topKFrequent(self, nums, k):
        nums.sort()
        freq = 0
        frequencies = []
        temp = nums[0]
        values = [temp]
        freqValues = []
        answer = []
        for i in range(len(nums)):
            if nums[i] == temp:
                freq += 1
            if nums[i] != temp or i == len(nums) - 1:
                temp = nums[i]
                values.append(temp)
                frequencies.append(freq)
                freq = 1
        frequencies.append(freq)
        for i in range(len(values)):
            freqValues.append([frequencies[i], values[i]])
        i = 1
        freqValues.sort()
        while i <= k:
            answer.append(freqValues[-i][1])
            i += 1

        return answer
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
