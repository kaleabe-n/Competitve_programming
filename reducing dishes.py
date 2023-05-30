class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        prefix = 0
        i = len(satisfaction)-1
        while i>=0 and satisfaction[i]>=0:
            prefix+=satisfaction[i]
            ans+=prefix
            i-=1
            
        while i>=0:
            prefix += satisfaction[i]
            if prefix>=0:
                ans+=prefix
            else:
                break
            i-=1
        return ans
        
        
