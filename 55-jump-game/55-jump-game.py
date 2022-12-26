class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        visited.add(0)
        stack = [0]
        while stack:
            curr = stack.pop()
            if curr == len(nums)-1:
                return True
            if nums[curr] == 0:
                continue
            for i in range(curr+1,min(len(nums),curr+nums[curr]+1)):
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return False
                
        
        