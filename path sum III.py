# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        stack = [root]
        total =  0
        while stack:
            curr = stack.pop()
            total+=dfs(curr,targetSum)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
        return total
            
        
        
def dfs(node,target):
    left = target-node.val
    if not node.right and not node.left:
        if left == 0:
            return 1
        return 0
    if left == 0:
        curr = 1
    else:
        curr = 0
    if node.right:
        curr += dfs(node.right,left)
    if node.left:
        curr += dfs(node.left,left)
        
    return curr
