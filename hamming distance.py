class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x or y:
            currX = x&1
            x = x>>1
            currY = y&1
            y = y>>1
            if currX!=currY:
                dist+=1
                
        return dist
