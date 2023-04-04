class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        ans = 0
        while num>0:
            if not num&1:
                ans+=mask
            num = num >> 1
            mask = mask << 1
            
        return ans
