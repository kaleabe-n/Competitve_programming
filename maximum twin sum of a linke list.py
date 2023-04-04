# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        prev = None
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            ne = slow.next
            slow.next = prev
            prev = slow
            slow = ne
        maxx = 0
        while prev:
            maxx = max(maxx,prev.val+slow.val)
            prev = prev.next
            slow = slow.next
            
        return maxx
