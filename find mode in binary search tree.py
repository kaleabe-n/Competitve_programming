# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = collections.defaultdict(int)
        stack = [root]
        while stack:
            curr = stack.pop()
            counts[curr.val]+=1
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        maxCount = max(counts.values())
        return [x for x in counts if counts[x] == maxCount]
        
