# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        pre = ListNode()
        pre.next = head
        current = pre_head
        
        while current is not None and current.next is not None and current.next.next is not None:
            temp = current.next
            current.next = temp.next
            temp.next = current.next.next
            current.next.next = temp
            current = temp
            
        return pre.next
            
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
