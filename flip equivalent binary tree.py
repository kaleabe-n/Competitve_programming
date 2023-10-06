# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not(root1 and root2) and (not root1 or not root2):
            return False
        if root1.val!=root2.val:
            return False
        return helper(root1,root2)
        
        
def helper(node1,node2):
    if not node1:
        return True
    n1l = node1.left.val if node1.left else None
    n2l = node2.left.val if node2.left else None
    n1r = node1.right.val if node1.right else None
    n2r = node2.right.val if node2.right else None
    if (n1l,n1r) == (n2l,n2r):
        ans = helper(node1.left,node2.left)
        ans = ans and helper(node1.right,node2.right)
    elif (n1l,n1r) == (n2r,n2l):
        ans = helper(node1.left,node2.right)
        ans = ans and helper(node1.right,node2.left)
    else:
        return False
    return ans
