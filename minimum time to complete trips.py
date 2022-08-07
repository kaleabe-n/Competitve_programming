class Solution(object):
    def minimumTime(self, time, totalTrips):
        left = 1
        right = totalTrips * min(time)
        while left<right:
            trips = 0
            mid = (left+right)//2
            for ti in time:
                trips+=mid//ti
            if trips>=totalTrips:
                right = mid
            else:
                left = mid+1
        return left
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        
