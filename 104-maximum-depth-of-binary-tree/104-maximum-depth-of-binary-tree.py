# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root)

def dfs(node):
    if node is None:
        return 0
    leftDepth = 0
    if node.left is not None:
        leftDepth = dfs(node.left)
    rightDepth = 0
    if node.right is not None:
        rightDepth = dfs(node.right)
    return (max(rightDepth,leftDepth)+1)