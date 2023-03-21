# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        dfs(root,self)
        return self.count
        
def dfs(node,obj):
    if not node.left and not node.right:
        obj.count+=1
        return {'sum':node.val,'count':1}
    if node.left:
        l = dfs(node.left,obj)
    else:
        l = {'sum':0,'count':0}
    if node.right:
        r = dfs(node.right,obj)
    else:
        r = {'sum':0,'count':0}
    currSum = l['sum']+r['sum']+node.val
    currCount = l['count']+r['count']+1
    if node.val == currSum//currCount:
        obj.count+=1
    return {'sum':currSum,'count':currCount}
        
