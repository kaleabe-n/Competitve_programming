# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def summm(node):
            if node.left is None and node.right is None:
                return node.val
            else:
                x=y=0
                if node.left is not None:
                    x=summm(node.left)
                if node.right is not None:
                    y=summm(node.right)
                return x+y+node.val
        summ=summm(root)
        self.ans=0
        def helper(node):
            if not node:
                return 0
            else:
                s=node.val+helper(node.left)+helper(node.right)
                self.ans=max(self.ans,(summ-s)*s)
                return s
        helper(root)
        return self.ans% (10**9+7)
            
            