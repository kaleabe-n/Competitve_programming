class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        if k==0:
            return 
        temp = nums[:len(nums)-k+1]
        for i in range(k):
            nums[i] = nums[(i+len(nums)-k)]
        ind = 0
        for i in range(k,len(nums)):
            nums[i] = temp[ind]
            ind+=1
            
        """
        Do not return anything, modify nums in-place instead.
        """
        
