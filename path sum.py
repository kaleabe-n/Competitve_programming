# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def find(node,summ,targetSum):
            if node == None:
                return
            if node.left == None and node.right == None:
                if summ+node.val == targetSum:
                    return True
            if node.left is not None:
                ans = find(node.left,summ+node.val,targetSum)
                if ans is not None:
                    return ans
            if node.right is not None:
                ans = find(node.right,summ+node.val,targetSum)
                if ans is not None:
                    return ans
        ans = find(root,0,targetSum)
        return ans if ans == True else False
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
