# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        counter = 1
        indNodePair = {}
        i = head
        while i is not None:
            indNodePair[counter] = i
            i = i.next
            counter+=1
        return indNodePair[counter//2] if counter%2==0 else indNodePair[counter//2+1]
        """
        :type head: ListNode
        :rtype: ListNode
        """
