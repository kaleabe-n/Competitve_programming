# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        ans = dfs(root)["swap"]
        ans[0].val,ans[1].val = ans[1].val,ans[0].val
                
def dfs(node):
    if node.left is None and node.right is None:
        return {"min":node,"max":node,"swap":None}
    ansl = None
    ansr = None
    if node.left is not None:
        ansl = dfs(node.left)
    if node.right is not None:
        ansr = dfs(node.right)
    if ansl is not None and ansr is not None:
        swap = ansl["swap"] if ansl["swap"] is not None else ansr["swap"]
        if ansl["max"].val > node.val:
            swap = [ansl["max"],node]
        if ansr["min"].val < node.val:
            swap = [ansr["min"],node]
        if ansl["max"].val>ansr["min"].val:
            swap = [ansl["max"],ansr["min"]]
        minn = min(ansl["min"],ansr["min"],node,key=lambda x:x.val)
        maxx = max(ansl["max"],ansr["max"],node,key=lambda x:x.val)
        return {"min":minn,"max":maxx,"swap":swap}
    if ansl is not None:
        minn = ansl["min"]
        maxx = ansl["max"]
    else:
        minn = ansr["min"]
        maxx = ansr["max"]
    if ansl is not None and ansl["max"].val > node.val:
        return {"min":min(minn,node,key = lambda x:x.val),"max":maxx,"swap":[ansl["max"],node]}
    if ansr is not None and ansr["min"].val < node.val:
        return {"min":minn,"max":max(maxx,node,key = lambda x:x.val),"swap":[ansr["min"],node]}
    swap  = None
    if ansl is not None:
        swap = ansl["swap"]
    if ansr is not None:
        swap = ansr["swap"]
    return {"min":min(minn,node,key = lambda x:x.val),"max":max(maxx,node,key = lambda x:x.val),"swap":swap}
    
    """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
