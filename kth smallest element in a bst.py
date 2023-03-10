# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        def recure(root,k,s,prevCount):
            count = 1
            if root.left:
                count+=recure(root.left,k,s,prevCount)
            if count+prevCount == k:
                s.ans = root.val
            if root.right:
                count+=recure(root.right,k,s,count+prevCount)
            return count
        recure(root,k,self,0)
        return self.ans
