class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr |= num
        self.count = 0
        for i in range(len(nums)):
            helper(nums,i,0,maxOr,self)
        return self.count
            
        
def helper(nums,ind,orVal,maxOr,obj):
    curr = orVal|nums[ind]
    if curr == maxOr:
        obj.count+=1
    for i in range(ind+1,len(nums)):
        helper(nums,i,curr,maxOr,obj)
            
   
