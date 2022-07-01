# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        nodes = []
        while temp is not None:
            nodes.append(temp)
            temp = temp.next
        if len(nodes) == 0:
            return
        else:
            nodes.sort(key=lambda x:x.val)
            head = nodes[0]
            temp = nodes[0]
            if len(nodes)>1:
                nodes.append(None)
                for i in range(0,len(nodes)-1):
                    temp.next = nodes[i+1]
                    temp = temp.next
        return head
        
