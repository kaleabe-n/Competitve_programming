# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ans = None
        head = None
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        i = list1
        j = list2
        if i.val<j.val:
            head = i
            ans = i
            head = i
            i = i.next
        else:
            head = j
            ans = j
            j = j.next
        while i is not None or j is not None:
            if i is None:
                ans.next = j
                ans =ans.next
                break
            elif j is None:
                ans.next = i
                ans = ans.next
                break
            elif i.val>=j.val:
                ans.next = j
                ans = ans.next
                j = j.next
            else:
                ans.next = i
                ans = ans.next
                i = i.next
        return head
                    
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
