# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        extra = 0
        dummy = ListNode(None)
        prevNode = dummy
        
        while l1 or l2:
            if not l1:
                currVal = extra+l2.val
                l2 = l2.next
            elif not l2:
                currVal = extra+l1.val
                l1 = l1.next
            else:
                currVal = extra+l1.val+l2.val
            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            extra = currVal//10
            prevNode.next = ListNode(currVal%10)
            prevNode = prevNode.next
            
            
        while extra>0:
            currVal = extra%10
            prevNode.next = ListNode(currVal)
            extra //= 10
            
        return dummy.next