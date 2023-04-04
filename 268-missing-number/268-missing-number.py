class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return [x for x in range(len(nums)+1) if x not in set(nums)][0]
        i = 0
        while i <len(nums):
            if nums[i]==len(nums):
                i+=1
                continue
            elif nums[i]!=i:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
            else:
                i+=1
        for i,num in enumerate(nums):
            if i!=num:
                return i
        return len(nums)
        


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         summ = sum(nums)
#         expSum = 0
#         i = 0
#         while i<=len(nums):
#             expSum+=i
#             i+=1
#         i = 0
#         while i<=len(nums):
#             if summ+i == expSum:
#                 return i
#             i+=1
            
        
