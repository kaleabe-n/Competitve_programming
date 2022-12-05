# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        if head.next.next == None:
            return head.next
        i = head
        j = head.next
        while j and j.next and j.next.next:
            j = j.next.next
            i = i.next
        return i.next