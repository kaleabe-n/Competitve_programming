# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = collections.deque()
        if root:
            que.append(root)
        tempQue = deque()
        rsv = []
        while que:
            rsv.append(que[-1].val)
            while que:
                curr = que.popleft()
                if curr.left:
                    tempQue.append(curr.left)
                if curr.right:
                    tempQue.append(curr.right)
            que,tempQue = tempQue,que
            
        return rsv
