# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTilt(self, root):
        def find(node):
            if node is None:
                return [0,0]
            if node.left is None:
                leftWeight = 0
                leftTilt = 0
            else:
                leftWeight,leftTilt = find(node.left)
            if node.right is None:
                rightWeight = 0
                rightTilt = 0
            else:
                rightWeight,rightTilt = find(node.right)
            return rightWeight+leftWeight+node.val,abs(rightWeight-leftWeight)+leftTilt+rightTilt
        return find(root)[1]
        """
        :type root: TreeNode
        :rtype: int
        """
        
