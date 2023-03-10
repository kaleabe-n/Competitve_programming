# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if not curr1 and not curr2:
                continue
            elif not curr1 or not curr2:
                return False
            elif curr1.val!=curr2.val:
                return False
            stack1.append(curr1.left)
            stack1.append(curr1.right)
            stack2.append(curr2.left)
            stack2.append(curr2.right)
        return True
