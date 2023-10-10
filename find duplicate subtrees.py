# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        traversals = {}
        return dfs(root,traversals)[1]
        
def dfs(node,traversals):
    if not node:
        return "None",[]
    curr = []
    left,lans = dfs(node.left,traversals)
    curr.append(left)
    right,rans = dfs(node.right,traversals)
    curr.append(right)
    curr.append(str(node.val))
    currans = ",".join(curr)
    lans.extend(rans)
    if currans in traversals:
        if traversals[currans]>=2:
            traversals[currans]+=1
            return currans,lans
        lans.append(node)
        traversals[currans]+=1
        return currans,lans
    traversals[currans] = 1
    return currans,lans
