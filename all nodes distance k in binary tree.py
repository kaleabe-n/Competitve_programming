# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        stack = [root]
        parent = {root:None}
        while stack:
            curr = stack.pop()
            if curr == target:
                break
            if curr.left:
                parent[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                parent[curr.right] = curr
                stack.append(curr.right)
                
        path = set()
        temp = target
        while temp:
            path.add(temp)
            temp = parent[temp]
        
        que = collections.deque([[root,k-len(path)+1]])
        ans = []
        while que:
            curr,l = que.popleft()
            if l == 0:
                ans.append(curr.val)
            if curr.left:
                added = -1
                if curr.left in path:
                    added = 1
                que.append([curr.left,l+added])
            if curr.right:
                added = -1
                if curr.right in path:
                    added = 1
                que.append([curr.right,l+added])
                
        return ans
            
            
