class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxLen = max([i[2] for i in trips])
        points = [0]*(maxLen+1)
        for i in range(len(trips)):
            points[trips[i][1]]+=trips[i][0]
            points[trips[i][2]]-=trips[i][0]
        prefixSum = 0
        for i in points:
            prefixSum+=i
            if prefixSum>capacity:
                return False
        return True