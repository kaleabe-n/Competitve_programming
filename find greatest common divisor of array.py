class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minn = float('inf')
        maxx = float('-inf')
        for num in nums:
            minn = min(minn,num)
            maxx = max(maxx,num)
            
        
        while minn>0:
            temp = maxx
            maxx = minn
            minn = temp%minn
                
        return maxx
            
