# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(dfs(root))
        
        
def dfs(node):
    if not node.left and not node.right:
        return [0,node.val]
    if node.left:
        left = dfs(node.left)
    else:
        left = [0,0]
    if node.right:
        right = dfs(node.right)
    else:
        right = [0,0]
    currIncluded = left[0]+right[0]+node.val
    withoutCurr = max(left)+max(right)
    return [withoutCurr,currIncluded]
