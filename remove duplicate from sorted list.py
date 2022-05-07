# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        i = head
        if i is not None:
            while i.next is not None:
                if i.val == i.next.val:
                    temp = i.next
                    i.next = i.next.next
                    temp.next = None
                else:
                    i = i.next
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
