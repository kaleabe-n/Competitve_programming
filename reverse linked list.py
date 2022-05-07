# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        i = head
        previous = None
        while i is not None:
            temp = i.next
            i.next = previous
            previous = i
            i = temp
            
        return previous
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
