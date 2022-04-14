class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        area = 0
        while start <= end:
            tempArea = min(height[start],height[end]) * (end-start)
            if tempArea>area:
                area = tempArea
            if height[start]<height[end]:
                start += 1
            else: 
                end -= 1
        return area
        """
        :type height: List[int]
        :rtype: int
        """
        
