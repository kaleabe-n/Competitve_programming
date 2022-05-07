# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode()
        ansHead = ans
        ext = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                temp = l2.val+ext
            elif l2 is None:
                temp = l1.val+ext
            else:
                temp = l1.val+l2.val+ext
            ans.val = temp%10
            ext =temp//10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is not None or l2 is not None:
                ans.next = ListNode()
                ans = ans.next
        if ext is not 0:
            ans.next = ListNode(ext)
        return ansHead
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
