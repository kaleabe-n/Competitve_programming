# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        fromLeft  = True
        que = collections.deque([root])
        ans = []
        while que:
            treeWidth = len(que)    #current level tree width
            subAns= []
            for i in range(treeWidth):
                if fromLeft:
                    current = que.popleft()
                    if current.left is not None:
                        que.append(current.left)
                    if current.right is not None:
                        que.append(current.right)
                else:
                    current = que.pop()
                    if current.right is not None:
                        que.appendleft(current.right)
                    if current.left is not None:
                        que.appendleft(current.left)
                subAns.append(current.val)
            fromLeft = not fromLeft
            ans.append(subAns)
        return ans
        