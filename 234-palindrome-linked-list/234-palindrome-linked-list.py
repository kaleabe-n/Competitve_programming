# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        prev=None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
        prev = None
        while slow:
            ne = slow.next
            slow.next = prev
            prev = slow
            if ne == None:
                break
            slow = ne
        while slow or head:
            if not slow:
                return True
            if not head:
                return True
            if slow.val != head.val:
                return False
            slow = slow.next
            head=head.next
        return True