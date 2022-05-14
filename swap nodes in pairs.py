# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        initial = ListNode()
        initial.next = head
        iterator = initial
        
        while iterator is not None and iterator.next is not None and iterator.next.next is not None:
            first = iterator.next
            second = iterator.next.next
            first.next = second.next
            second.next = first
            iterator.next = second
            iterator = first
        
        return initial.next
            
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
