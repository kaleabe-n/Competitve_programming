# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que = collections.deque()
        que.append(root)
        tempQue = collections.deque()
        while que:
            l = 0
            r = len(que)-1
            while l<r:
                if que[l] is None and que[r] is None:
                    l+=1
                    r-=1
                elif not que[l] or not que[r]:
                    return False
                elif que[l].val != que[r].val:
                    return False
                else:
                    l+=1
                    r-=1
            while que:
                curr = que.popleft()
                if curr is None:
                    continue
                tempQue.append(curr.left)
                tempQue.append(curr.right)
                
            del que
            que = tempQue
            tempQue = collections.deque()
            
        return True





# from collections import deque

# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def isSymmetric(self, root):
#         left = deque([[root.left,"l"]])
#         right = deque([[root.right,"r"]])
#         while len(left)>0 and len(right)>0:
#             l = left.pop()
#             r = right.pop()
#             if l[0] is not None:
#                 left.append([l[0].right,"r"])
#                 left.append([l[0].left,"l"])
#             if r[0] is not None:
#                 right.append([r[0].left,"l"])
#                 right.append([r[0].right,"r"])
#             leftvalue = l[0].val if l[0] is not None else l[0]
#             rightvalue = r[0].val if r[0] is not None else r[0]
#             if leftvalue != rightvalue:
#                 return False
#         if len(left)!=len(right):
#             return False
#         return True
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
        
