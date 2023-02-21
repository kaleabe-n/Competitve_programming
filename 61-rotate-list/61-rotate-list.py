# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeCount = 0
        temp = head
        if head is None:
            return None
        while temp:
            nodeCount+=1
            temp = temp.next
        k = k % nodeCount
        if k == 0:
            return head
        ind = -1
        dummy = ListNode(None,head)
        fast = dummy
        slow = None
        while fast and fast.next:
            ind+=1
            if ind == k:
                slow=head
            elif slow:
                slow = slow.next
            fast = fast.next
        fast.next = head
        dummy.next = slow.next
        slow.next = None
        return dummy.next