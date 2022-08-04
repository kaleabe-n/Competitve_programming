# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for li in lists:
            item = li
            while item is not None:
                heapq.heappush(heap,item.val)
                item = item.next
        if len(heap) == 0:
            return None
        ans = ListNode(heapq.heappop(heap))
        i = 0
        le = len(heap)
        temp = ans
        while i<le:
            temp.next = ListNode(heapq.heappop(heap))
            temp = temp.next
            i+=1
        return ans
        
            
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
