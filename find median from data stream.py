class MedianFinder:

    def __init__(self):
        self.leftheap = []
        self.rightheap = []

    def addNum(self, num: int) -> None:
        if not self.rightheap or num <= self.rightheap[0]:
            heapq.heappush(self.leftheap,-num)
        else:
            heapq.heappush(self.rightheap,num)
        if len(self.leftheap)<len(self.rightheap):
            temp = heapq.heappop(self.rightheap)
            heapq.heappush(self.leftheap,-temp)
        if len(self.rightheap)+1<len(self.leftheap):
            temp = heapq.heappop(self.leftheap)
            heapq.heappush(self.rightheap,-temp)
            
        
        

    def findMedian(self) -> float:
        if len(self.rightheap) == len(self.leftheap):
            return (-self.leftheap[0]+self.rightheap[0])/2
        else:
            return -self.leftheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# import heapq

# class MedianFinder(object):

#     def __init__(self):
#         self.belowMed = []
#         self.aboveMed = []
        

#     def addNum(self, num):
#         if len(self.belowMed) == len(self.aboveMed):
#             if len(self.belowMed) == 0 or num <= self.aboveMed[0]:
#                 heapq.heappush(self.belowMed,-num)
#             else:
#                 heapq.heappush(self.aboveMed,num)
#         elif len(self.belowMed) < len(self.aboveMed):
#             if num <= self.aboveMed[0]:
#                 heapq.heappush(self.belowMed,-num)
#             else:
#                 val = heapq.heapreplace(self.aboveMed,num)
#                 heapq.heappush(self.belowMed,-val)
#         else:
#             if num>=-self.belowMed[0]:
#                 heapq.heappush(self.aboveMed,num)
#             else:
#                 val = heapq.heapreplace(self.belowMed,-num)
#                 heapq.heappush(self.aboveMed,-val)
#         """
#         :type num: int
#         :rtype: None
#         """
        

#     def findMedian(self):
#         if len(self.belowMed) == len(self.aboveMed):
#             return (-(self.belowMed[0]) + self.aboveMed[0]) / 2.0
#         elif len(self.belowMed) > len(self.aboveMed):
#             return -self.belowMed[0]
#         else:
#             return self.aboveMed[0]
        
#         """
#         :rtype: float
#         """
        


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()
