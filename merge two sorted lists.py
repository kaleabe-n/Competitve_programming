# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(merged,l1,l2):
            if l1 is None and l2 is None:
                return 
            elif l1 is None:
                merged.next = ListNode(l2.val)
                l2 = l2.next
                helper(merged.next,l1,l2)
            elif l2 is None or l1.val <= l2.val:
                merged.next = ListNode(l1.val)
                l1 = l1.next
                helper(merged.next,l1,l2)
            else:
                merged.next = ListNode(l2.val)
                l2 = l2.next
                helper(merged.next,l1,l2)
        dummy = ListNode()
        temp = dummy
        helper(temp,list1,list2)
        return dummy.next
