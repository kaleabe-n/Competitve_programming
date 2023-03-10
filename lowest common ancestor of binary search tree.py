# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def recure(root,p,q,s):
            if root == None:
                return False
            curr = root == p or root == q
            left = recure(root.left,p,q,s)
            right = recure(root.right,p,q,s)
            if curr and left or curr and right or left and right and s.lca == None:
                s.lca = root
            return curr or left or right
        recure(root,p,q,self)
        return self.lca
