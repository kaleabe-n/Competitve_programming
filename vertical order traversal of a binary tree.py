# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversals = collections.defaultdict(list)
        que = collections.deque([(root,0,0)])
        while que:
            curr,ind,lvl = que.popleft()
            traversals[ind].append((lvl,curr.val))
            if curr.left:
                que.append((curr.left,ind-1,lvl+1))
            if curr.right:
                que.append((curr.right,ind+1,lvl+1))
        ans = []
        inds = list(traversals.keys())
        inds.sort()
        for i in inds:
            nodes = traversals[i]
            traversals[i].sort()
            ans.append([x[1] for x in traversals[i]])
        
        return ans
            
