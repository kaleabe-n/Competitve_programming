# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        helper(root,0,self)
        return self.sum
        
def helper(node,prevSum,obj):
    prevSum*=10
    prevSum+=node.val
    if not node.left and not node.right:
        obj.sum+=prevSum
    else:
        if node.left:
            helper(node.left,prevSum,obj)
        if node.right:
            helper(node.right,prevSum,obj)
