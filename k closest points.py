class Solution(object):
    def kClosest(self, points, k):
        points.sort(key = lambda x:sqrt(x[0]**2 + x[1]**2))
        return points[:k]
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
