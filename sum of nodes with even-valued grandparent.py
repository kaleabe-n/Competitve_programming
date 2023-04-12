# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return dfs(root,1,1)
        
        
def dfs(node,p,gp):
    ans = 0
    if gp % 2 == 0:
        ans += node.val
    if node.left:
        ans += dfs(node.left,node.val,p)
    right = 0
    if node.right:
        ans += dfs(node.right,node.val,p)
    return ans
    






# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def sumEvenGrandparent(self, root):
#         def dfs(node):
#             if node.left is None and node.right is None:
#                 return {"total":0,"high":node.val,"low":0}
#             if node.left is not None:
#                 ans = dfs(node.left)
#                 leftLow = ans["low"]
#                 leftHigh = ans["high"]
#                 leftTotal =ans["total"]
#             else:
#                 leftLow = 0
#                 leftHigh = 0
#                 leftTotal = 0
            
#             if node.right is not None:
#                 ans = dfs(node.right)
#                 rightLow = ans["low"]
#                 rightHigh = ans["high"]
#                 rightTotal =ans["total"]
#             else:
#                 rightLow = 0
#                 rightHigh = 0
#                 rightTotal = 0
#             ans = {}
#             ans["total"] = rightTotal+leftTotal+rightLow+leftLow if node.val%2 == 0 else rightTotal+leftTotal
#             ans["low"] = rightHigh + leftHigh
#             ans["high"] = node.val
#             return ans
#         return dfs(root)["total"]
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
        
