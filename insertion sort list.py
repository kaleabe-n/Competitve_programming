# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = head
        temp = head.next
        while temp is not None:
            notChanged = True
            prev = ListNode(None,head)
            temp2 = head
            while temp2 is not temp:
                if temp.val<temp2.val:
                    notChanged = False
                    if temp2 == head:
                        head = temp
                    prev.next = temp
                    previous.next = temp.next
                    temp.next = temp2
                    temp = previous.next
                    break
                prev = prev.next
                temp2 = temp2.next
            if notChanged:
                previous = previous.next
                temp = temp.next
        return head
                    
                    
            
