# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    minD = float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def preOrder(obj,node):
            curr = node.val
            values = [curr]
            if node.left is not None:
                left = preOrder(obj,node.left)
                values.extend(left)
                obj.minD = min(obj.minD,curr-left[1])
            if node.right is not None:
                right = preOrder(obj,node.right)
                values.extend(right)
                obj.minD = min(obj.minD,right[0]-curr)
            return [min(values),max(values)]
        preOrder(self,root)
        return self.minD
    