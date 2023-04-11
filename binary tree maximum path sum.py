# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')
        dfs(root,self)
        return self.max
        
        
def dfs(node,obj):
    if not node:
        return 0
    left = dfs(node.left,obj)
    right = dfs(node.right,obj)
    
    obj.max = max(obj.max,left+right+node.val)
    return max(0,node.val+right,node.val+left)
