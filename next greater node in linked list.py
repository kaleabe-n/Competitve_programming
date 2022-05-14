# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        counter = 0
        temp = head
        while temp is not None:
            counter+=1
            temp = temp.next
        ans = [0]*counter
        temp = head
        counter = 0
        monSta = []
        indSta = []
        while temp is not None:
            if len(monSta)==0:
                monSta.append(temp)
                indSta.append(counter)
            elif temp.val<=monSta[-1].val:
                monSta.append(temp)
                indSta.append(counter)
            else:
                while monSta and temp.val>monSta[-1].val:
                    monSta.pop()
                    ans[indSta.pop()]=temp.val
                monSta.append(temp)
                indSta.append(counter)
            counter+=1
            temp = temp.next
        return ans
            
        """
        :type head: ListNode
        :rtype: List[int]
        """
        
