class Solution(object):
    def longestSubarray(self, nums, limit):
        i = 0
        j = 0
        maxx = 0
        maxQue = []
        minQue = []
        while j<len(nums):
            if len(minQue)==0:
                minQue.append(nums[j])
            elif nums[j]>=minQue[-1]:
                minQue.append(nums[j])
            else:
                while nums[j]<minQue[-1]:
                    minQue.pop()
                    if len(minQue)==0:
                        break
                minQue.append(nums[j])
            if len(maxQue)==0:
                maxQue.append(nums[j])
            elif nums[j]<=maxQue[-1]:
                maxQue.append(nums[j])
            else:
                while nums[j]>maxQue[-1]:
                    maxQue.pop()
                    if len(maxQue)==0:
                        break
                maxQue.append(nums[j])
            if maxQue[0]-minQue[0]<=limit:
                if j-i+1>maxx:
                    maxx = j-i+1
            else:
                if maxQue[0] == nums[i]:
                    maxQue.pop(0)
                if minQue[0] == nums[i]:
                    minQue.pop(0)
                i+=1
            j+=1
        return maxx
            
            
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
