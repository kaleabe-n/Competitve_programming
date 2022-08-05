"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution(object):
    def findSolution(self, customfunction, z):
        ans = []
        for i in range(1,1000):
            left = 1
            right = 1000
            while left<right:
                if customfunction.f(i,(left+right)//2) < z:
                    if customfunction.f(i,(left+right)//2+1) > z:
                        left = (left+right)//2+1
                        break
                    else:
                        left = (left+right)//2+1
                else:
                    right = (left+right)//2
            if customfunction.f(i,left) == z:
                ans.append([i,left])
        return ans
                    
                        
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        
