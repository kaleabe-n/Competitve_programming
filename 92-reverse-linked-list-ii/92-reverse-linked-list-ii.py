# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        reversing = False
        i = 0
        temp = dummy
        while temp is not None:
            if i == left-1:
                preRev = temp
                prev = None
                reversing = True
                temp = temp.next
                revFirst = temp
            elif reversing:
                ne=temp.next
                temp.next = prev
                prev = temp
                temp = ne
                if i == right:
                    preRev.next = prev
                    revFirst.next = temp
                    break
            else:
                temp = temp.next
            i+=1
        return dummy.next