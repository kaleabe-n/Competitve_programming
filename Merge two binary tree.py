# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def recure(root1,root2,merged):
            if not root1:
                return root2
            elif not root2:
                return root1
            else:
                merged.val = root1.val+root2.val
                merged.left = recure(root1.left,root2.left,TreeNode())
                merged.right = recure(root1.right,root2.right,TreeNode())
                return merged
        return recure(root1,root2,TreeNode())
