class Solution(object):
    def isCovered(self, ranges, left, right):
        ranges.sort()
        prefixRanges = []
        for i in ranges:
            if len(prefixRanges) == 0:
                prefixRanges.append(i)
            else:
                if hasOverlap(prefixRanges[-1],i):
                    prefixRanges[-1] = union(prefixRanges[-1],i)
                else:
                    prefixRanges.append(i)
        mainRange = [left,right]
        intRange = None
        for i in prefixRanges:
            if hasOverlap(i,mainRange) and intersection(i,mainRange) == mainRange:
                return True
        return False
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
def hasOverlap(range1,range2):
    if range1[1]+1>=range2[0] and range2[1]+1>=range1[0]:
        return True
    return False
def union(range1,range2):
    return [min(range1[0],range2[0]),max(range1[1],range2[1])]
def intersection(range1,range2):
    return [max(range1[0],range2[0]),min(range1[1],range2[1])]