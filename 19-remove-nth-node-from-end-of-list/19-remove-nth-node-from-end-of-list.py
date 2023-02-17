# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = None
        i = -1
        n-=1
        dummy = ListNode(None,head)
        fast = dummy
        prev = dummy
        while fast is not None:
            i+=1
            if i == n:
                slow = head
            elif fast.next == None:
                prev.next = slow.next
                break
            elif i>n:
                prev = slow
                slow = slow.next
            fast = fast.next
        return dummy.next