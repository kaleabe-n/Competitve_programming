# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        return dfs(root,0)["lca"]
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
    
    
def dfs(node,depthCount):
    depthCount+=1
    if node.left is None and node.right is None:
        return {"maxDepth":depthCount,"lca":node}
    if node.left is not None:
        ans = dfs(node.left,depthCount)
        leftDepth = ans["maxDepth"]
        leftLca = ans["lca"]
    if node.right is not None:
        ans = dfs(node.right,depthCount)
        rightDepth = ans["maxDepth"]
        rightLca = ans["lca"]
    if node.left is None or node.right is None or rightDepth > leftDepth:
        return ans
    if leftDepth == rightDepth:
        return {"maxDepth":leftDepth,"lca":node}
    if leftDepth > rightDepth:
        return {"maxDepth":leftDepth,"lca":leftLca}
