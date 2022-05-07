# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        i = head
        j = head
        prev = None
        for k in range(n):
            i = i.next
        while i is not None:
            prev = j
            j = j.next
            i = i.next
        if j.next is None:
            if prev == None:
                head = None
            else:
                prev.next = None
        elif j.next is not None:
            j.val = j.next.val 
            j.next = j.next.next
        return head
            
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
