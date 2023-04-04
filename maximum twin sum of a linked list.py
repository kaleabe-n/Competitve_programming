# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        prev = None
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            ne = slow.next
            slow.next = prev
            prev = slow
            slow = ne
        maxx = 0
        while prev:
            maxx = max(maxx,prev.val+slow.val)
            prev = prev.next
            slow = slow.next
            
        return maxx




# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def pairSum(self, head):
#         mid = head
#         j = head.next
#         while j is not None and j.next is not None:
#             j = j.next.next
#             mid = mid.next
#         nextStart = mid.next
#         mid.next = None
        
#         temp = head
#         prev = None
#         while temp is not None:
#             nxt = temp.next
#             temp.next = prev
#             prev = temp
#             temp = nxt
            
                
#         back = mid
#         fore = nextStart
#         maxx = 0
#         while back is not None and fore is not None:
#             if back.val+fore.val > maxx:
#                 maxx = back.val+fore.val
#             back = back.next
#             fore = fore.next
#         return maxx
#         """
#         :type head: Optional[ListNode]
#         :rtype: int
#         """
        
