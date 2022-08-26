from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        left = deque([[root.left,"l"]])
        right = deque([[root.right,"r"]])
        while len(left)>0 and len(right)>0:
            l = left.pop()
            r = right.pop()
            if l[0] is not None:
                left.append([l[0].right,"r"])
                left.append([l[0].left,"l"])
            if r[0] is not None:
                right.append([r[0].left,"l"])
                right.append([r[0].right,"r"])
            leftvalue = l[0].val if l[0] is not None else l[0]
            rightvalue = r[0].val if r[0] is not None else r[0]
            if leftvalue != rightvalue:
                return False
        if len(left)!=len(right):
            return False
        return True
        """
        :type root: TreeNode
        :rtype: bool
        """
        
