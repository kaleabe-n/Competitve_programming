# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        que = collections.deque([(root,0)])
        tempQue = collections.deque()
        while que:
            minInd = float('inf')
            maxInd = float('-inf')
            while que:
                curr,ind = que.popleft()
                if curr.left:
                    tempQue.append((curr.left,ind*2))
                if curr.right:
                    tempQue.append((curr.right,ind*2+1))
                minInd = min(ind,minInd)
                maxInd = max(ind,maxInd)
            maxWidth = max(maxWidth,maxInd-minInd+1)
            que,tempQue = tempQue,que
            
            
        return maxWidth
