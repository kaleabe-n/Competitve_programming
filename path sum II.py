# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = dfs(root,0,targetSum)
        for i in range(len(ans)):
            ans[i].reverse()
        return ans
        
def dfs(node,currSum,target):
    currSum +=node.val
    if not node.left and not node.right:
        if currSum == target:
            return [[node.val]]
        else:
            return []
    curr = []
    if node.left:
        left = dfs(node.left,currSum,target)
        for i in range(len(left)):
            left[i].append(node.val)
        curr = left
    if node.right:
        right = dfs(node.right,currSum,target)
        for i in range(len(right)):
            right[i].append(node.val)
        curr.extend(right)
    return curr
