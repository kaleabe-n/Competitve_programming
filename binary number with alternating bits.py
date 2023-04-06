class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n>0:
            curr = n&1
            if curr == prev:
                return False
            prev = curr
            n>>=1
            
        return True
