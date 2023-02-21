# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        temp = head
        monSta = []
        indSta = []
        ind = 0
        while temp:
            while monSta and monSta[-1] < temp.val:
                monSta.pop()
                i = indSta.pop()
                answer[i] = temp.val
            answer.append(0)
            monSta.append(temp.val)
            indSta.append(ind)
            ind+=1
            temp = temp.next
        return answer