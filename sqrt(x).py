class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x+1
        while left<=right:
            mid = (left+right)//2
            if mid*mid > x:
                if (mid-1)*(mid-1)>=x:
                    right = mid-1
                else:
                    return mid-1
            elif mid*mid < x:
                if (mid+1)*(mid+1)<=x:
                    left = mid+1
                else:
                    return mid
            else:
                return mid
        
