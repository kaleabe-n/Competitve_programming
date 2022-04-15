class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h = 0
        for i in range(len(citations)):
            temp = len(citations[i:])
            if temp<=citations[i]:
                return temp
        return 0
        """
        :type citations: List[int]
        :rtype: int
        """
        
