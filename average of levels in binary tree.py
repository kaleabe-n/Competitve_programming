from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        ans = []
        que = deque([root])
        treeWidth = 1
        count = 0
        numsCount = 0
        rowSum = 0
        valueExists = False
        noneCount = 0
        while que:
            current = que.popleft()
            if current is not None:
                valueExists = True
                que.append(current.left)
                que.append(current.right)
                rowSum+=current.val
                numsCount+=1
            else:
                noneCount+=1
            count+=1
            if count == treeWidth:
                if valueExists:
                    ans.append(float(rowSum)/numsCount)
                numsCount = 0
                rowSum = 0
                count = 0
                treeWidth-=noneCount
                noneCount = 0
                treeWidth = 2*treeWidth
                valueExists = False
        if rowSum!=0 and valueExists:
            ans.append(rowSum/numsCount)
        return ans
            
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
