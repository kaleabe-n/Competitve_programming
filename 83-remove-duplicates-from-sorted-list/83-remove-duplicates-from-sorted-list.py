# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        nonRemoved = head
        removing = False
        while temp:
            if temp.next == None:
                if removing:
                    nonRemoved.next = None
                    break
            elif removing:
                if temp.val != temp.next.val:
                    nonRemoved.next = temp.next
                    removing = False
            elif temp.val == temp.next.val:
                removing = True
                nonRemoved = temp
            temp = temp.next
        return head