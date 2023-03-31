# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        l = 0
        temp = head
        while temp:
            l+=1
            temp = temp.next
        return mergesort(head,l)
    
    
def mergesort(head,length):
    if length == 1:
        return head
    if not head:
        return
    mid = length // 2
    m = mid
    temp = head
    while temp:
        mid-=1
        if mid == 0:
            right = temp.next
            temp.next = None
            break
        temp = temp.next
    left = head
    left = mergesort(left,m)
    right = mergesort(right,length-m)
    merged = merge(left,right)
    return merged
    

def merge(left,right):
    dummy = ListNode(None)
    temp = dummy
    while left and right:
        if left.val <= right.val:
            temp.next = left
            left = left.next
            temp.next.next = None
        else:
            temp.next = right
            right =  right.next
            temp.next.next = None
        temp = temp.next
    if left:
        temp.next = left
    else:
        temp.next = right
    return dummy.next

    





# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp = head
#         nodes = []
#         while temp is not None:
#             nodes.append(temp)
#             temp = temp.next
#         if len(nodes) == 0:
#             return
#         else:
#             nodes.sort(key=lambda x:x.val)
#             head = nodes[0]
#             temp = nodes[0]
#             if len(nodes)>1:
#                 nodes.append(None)
#                 for i in range(0,len(nodes)-1):
#                     temp.next = nodes[i+1]
#                     temp = temp.next
#         return head
        
