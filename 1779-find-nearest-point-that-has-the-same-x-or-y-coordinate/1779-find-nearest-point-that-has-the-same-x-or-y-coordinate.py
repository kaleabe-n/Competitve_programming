class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minn = float('inf')
        ans = None
        for i in range(len(points)):
            if points[i][0] == x:
                newMin = abs(points[i][1]-y)
            elif points[i][1] == y:
                newMin = abs(points[i][0]-x)
            else:
                newMin = float('inf')
            if newMin < minn:
                minn = newMin
                ans = i
        return -1 if minn == float('inf') else ans