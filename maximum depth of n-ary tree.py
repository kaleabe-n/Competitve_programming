"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return helper(root)
        
        
def helper(node):
    if not node:
        return 0
    maxx = 0
    for child in node.children:
        maxx = max(maxx,helper(child))
    return maxx+1



# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children
# """

# class Solution(object):
#     def maxDepth(self, root):
#         def counter(node,count,maxx):
#             if node is None:
#                 return count
#             if len(node.children) == 0:
#                 return count+1
#             for child in node.children:
#                 ans = counter(child,count+1,maxx)
#                 maxx = max(maxx,ans)
#             return maxx
#         return counter(root,0,0)
#         """
#         :type root: Node
#         :rtype: int
#         """
        
