# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root)[2]
        
def helper(node):
    minn = node.val
    maxx = node.val
    isValid = True
    if node.left:
        lmin,lmax,lisValid = helper(node.left)
        if node.val<=lmax:
            isValid = False
        minn = min(minn,lmin)
        isValid = isValid and lisValid
    if node.right:
        rmin,rmax,risValid = helper(node.right)
        if node.val>=rmin:
            isValid = False
        maxx = max(node.val,rmax)
        isValid = isValid and risValid
    return [minn,maxx,isValid]



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.ans = True
#         def recure(root,s):
#             if not root.left:
#                 left = {'max':float('-inf'),'min':float('inf')}
#             else:
#                 left = recure(root.left,s)
#             if not root.right:
#                 right = {'min':float('inf'),'max':float('-inf')}
#             else:
#                 right = recure(root.right,s)
            
#             if right['min']<=left['max'] or right['min']<=root.val or left['max']>=root.val:
#                 s.ans = False
#             return {'min':min(left['min'],root.val),'max':max(right['max'],root.val)}
#         recure(root,self)
#         return self.ans
