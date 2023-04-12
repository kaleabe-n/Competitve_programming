# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        helper(root,ans)
        return "".join(ans)

def helper(node,ans):
    ans.append(str(node.val))
    if not node.left and not node.right:
        return
    if node.left:
        ans.append("(")
        helper(node.left,ans)
        ans.append(")")
    else:
        ans.append("(")
        ans.append(")")
    if node.right:
        ans.append("(")
        helper(node.right,ans)
        ans.append(")")
