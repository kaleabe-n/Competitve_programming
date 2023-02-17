# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode(None)
        merged = dummy
        while temp1 is not None or temp2 is not None:
            if temp1 is None:
                ne = temp2.next
                merged.next = temp2
                merged = merged.next
                temp2 = ne
            elif temp2 is None or temp2.val > temp1.val:
                ne = temp1.next
                merged.next = temp1
                merged = merged.next
                temp1 = ne
            else:
                ne = temp2.next
                merged.next = temp2
                merged = merged.next
                temp2 = ne
        return dummy.next
                