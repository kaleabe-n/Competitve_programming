# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = collections.deque([root])
        tempQue = collections.deque()
        ans = []
        while que:
            ans.append([x.val for x in que])
            while que:
                curr = que.popleft()
                if curr.left:
                    tempQue.append(curr.left)
                if curr.right:
                    tempQue.append(curr.right)
            que,tempQue = tempQue,que
            
        return ans
