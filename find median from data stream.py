import heapq

class MedianFinder(object):

    def __init__(self):
        self.belowMed = []
        self.aboveMed = []
        

    def addNum(self, num):
        if len(self.belowMed) == len(self.aboveMed):
            if len(self.belowMed) == 0 or num <= self.aboveMed[0]:
                heapq.heappush(self.belowMed,-num)
            else:
                heapq.heappush(self.aboveMed,num)
        elif len(self.belowMed) < len(self.aboveMed):
            if num <= self.aboveMed[0]:
                heapq.heappush(self.belowMed,-num)
            else:
                val = heapq.heapreplace(self.aboveMed,num)
                heapq.heappush(self.belowMed,-val)
        else:
            if num>=-self.belowMed[0]:
                heapq.heappush(self.aboveMed,num)
            else:
                val = heapq.heapreplace(self.belowMed,-num)
                heapq.heappush(self.aboveMed,-val)
        """
        :type num: int
        :rtype: None
        """
        

    def findMedian(self):
        if len(self.belowMed) == len(self.aboveMed):
            return (-(self.belowMed[0]) + self.aboveMed[0]) / 2.0
        elif len(self.belowMed) > len(self.aboveMed):
            return -self.belowMed[0]
        else:
            return self.aboveMed[0]
        
        """
        :rtype: float
        """
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
