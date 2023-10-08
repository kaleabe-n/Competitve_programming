# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return dfs(p,q,root)[2]
        
def dfs(p,q,node):
    if node in (p,q):
        curr = True
    else:
        curr = False
    if node.left:
        left,both,ans = dfs(p,q,node.left)
        if both:
            return [left,both,ans]
    else:
        left = False
    if node.right:
        right,both,ans = dfs(p,q,node.right)
        if both:
            return [right,both,ans]
    else:
        right = False
    if (left and right) or (curr and (left or right)):
        return [True,True,node]
    else:
        return [curr or left or right,False,None]
