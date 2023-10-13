# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            left,ldist = dfs(node.left)
            right,rdist = dfs(node.right)
            count = node.val + left + right - 1
            totalDist = ldist + rdist + abs(count)  
            return [count,totalDist]
        return dfs(root)[1]
