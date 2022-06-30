# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next  is None:
            return head
        if head.next.val == head.val:
            temp = head
            while temp is not None and temp.val == head.val:
                temp = temp.next
            head.val = None
            head.next = temp
            if temp is None:
                return
        curr = head
        prev = None
        while curr is not None and curr.next is not None:
            repeated = False
            if curr.val != curr.next.val:
                prev = curr
                temp = curr.next
                #repeatedNode will be the last of the repeated nodes now it just holds the node before the repeated node
                repeatedNode = curr
                while temp.next is not None and temp.val == temp.next.val:
                    repeated = True
                    temp = temp.next
                    repeatedNode = repeatedNode.next
                if repeated:
                    repeatedNode.next = None
                    prev.next = temp.next
                else:
                    curr = curr.next
        return head if head.val is not None else head.next
                    
                
