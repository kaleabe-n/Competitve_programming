class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monSta = []
        minn = float('inf')
        
        for num in nums:
            while monSta and monSta[-1][0]<=num:
                monSta.pop()
            if monSta and num > monSta[-1][1]:
                return True
            minn = min(minn,num)
            monSta.append([num,minn])
            
        return False
